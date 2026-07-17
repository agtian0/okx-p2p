---
name: okx-p2p
description: Use when working with the OKX P2P trading API — ad creation, order management, disputes, chat, file uploads, user management, payment methods, and configuration.
---

# OKX P2P Trading API Skill

Use when integrating with or building applications that interact with the OKX Peer-to-Peer (P2P) trading platform. This skill provides comprehensive coverage of the OKX P2P API including ad creation, order management, dispute handling, chat functionality, and user management.

## 💡 When to Use This Skill

Use this skill when you need to:
- Create and manage P2P advertisements (buy/sell ads)
- Handle P2P order lifecycle (creation, payment, completion, appeals)
- Manage user profiles, blacklists, and verification settings
- Implement real-time chat between trading parties
- Handle file uploads for verification purposes
- Process dispute resolution workflows
- Retrieve market data and trading statistics
- Configure payment methods and pricing strategies

## 📚 Documentation Coverage

This skill covers **86 pages** of OKX P2P API documentation including:

- **Ad Management** (Create, Get, Update, Cancel ads)
- **Order Management** (Create, Cancel, Payment confirmation, Crypto release)
- **Dispute System** (Create, Cancel, Message disputes)
- **Chat System** (Send messages, Get chat history)
- **File Upload** (Verification documents, evidence)
- **User Management** (Blacklist, verification status, statistics)
- **Merchant Tools** (Following status, basic info updates)
- **Payment Methods** (Configuration, updates)
- **Configuration Endpoints** (Price scales, limits, available values)

## 🚀 Quick Start Examples

### Create a P2P Advertisement
```bash
POST /api/v5/p2p/ad/create
Content-Type: application/json

{
  "cryptoCurrency": "USDT",
  "fiatCurrency": "USD",
  "side": "sell",
  "amount": "1000",
  "price": "1.0",
  "minOrderLimit": "10",
  "maxOrderLimit": "500",
  "paymentMethodIds": ["123", "456"],
  "message": "Payment via bank transfer please",
  "isPublic": true
}
```

### Create a P2P Order (Buy Crypto)
```bash
POST /api/v5/p2p/order/create
Content-Type: application/json

{
  "adId": "123456789",
  "side": "buy",
  "amount": "500",
  "price": "1.0"
}
```

### Confirm Payment Received
```bash
POST /api/v5/p2p/order/mark-as-paid
Content-Type: application/json

{
  "orderId": "ORDER123",
  "paymentTime": "1620000000000"
}
```

### Release Crypto After Payment Confirmation
```bash
POST /api/v5/p2p/order/release-crypto
Content-Type: application/json

{
  "orderId": "ORDER123"
}
```

### Send Message to Counterparty
```bash
POST /api/v5/p2p/chat/send-message
Content-Type: application/json

{
  "orderId": "ORDER123",
  "content": "Payment sent, please check your account",
  "contentType": "101"
}
```

### Upload Verification Document
```bash
POST /api/v5/p2p/file/upload
Content-Type: multipart/form-data

file: [verification.jpg]
```

## 📖 API Categories & Endpoints

### 📢 Advertisement Management
- `POST /api/v5/p2p/ad/create` - Create new P2P advertisement
- `GET /api/v5/p2p/ad` - Get advertisement details by ID
- `POST /api/v5/p2p/ad/update` - Update advertisement details
- `POST /api/v5/p2p/ad/update-active-status` - Toggle ad active/paused status
- `POST /api/v5/p2p/ad/cancel` - Cancel/delete advertisement

### 📋 Order Management
- `POST /api/v5/p2p/order/create` - Create new P2P order
- `POST /api/v5/p2p/order/cancel` - Cancel P2P order
- `POST /api/v5/p2p/order/mark-as-paid` - Mark order as paid by buyer
- `POST /api/v5/p2p/order/mark-as-unpaid` - Mark order as unpaid
- `POST /api/v5/p2p/order/release-crypto` - Release cryptocurrency to buyer
- `POST /api/v5/p2p/order/counterparty-user-list` - Get counterparty user list for an order

### ⚖️ Dispute Management
- `POST /api/v5/p2p/dispute/create` - Create dispute for an order
- `POST /api/v5/p2p/dispute/cancel` - Cancel an existing dispute
- `POST /api/v5/p2p/dispute/sendMessage` - Send message in dispute chat

### 💬 Chat System
- `GET /api/v5/p2p/chat/history` - Get chat history for an order
- `POST /api/v5/p2p/chat/send-message` - Send message to counterparty

### 📎 File Management
- `POST /api/v5/p2p/file/upload` - Upload files (ID proof, payment receipts, etc.)

### 👤 User Management
- `GET /api/v5/p2p/user/id` - Get user ID information
- `GET /api/v5/p2p/user/blacklist-users` - Get user's blacklist
- `POST /api/v5/p2p/user/add-user-to-blacklist` - Add user to blacklist
- `POST /api/v5/p2p/user/remove-user-from-blacklist` - Remove user from blacklist
- `GET /api/v5/p2p/user/statistics` - Get user trading statistics
- `GET /api/v5/p2p/user/basic-info` - Get basic user information
- `POST /api/v5/p2p/user/update-online-status` - Update user online status

### 🏪 Merchant Tools
- `POST /api/v5/p2p/merchant/update-basic-info` - Update merchant basic information
- `POST /api/v5/p2p/merchant/update-following-status` - Update merchant following status

### 💳 Payment Methods
- `POST /api/v5/p2p/payment-method/update` - Update payment method details

### ⚙️ Configuration
- `GET /api/v5/p2p/config` - Get system configuration (limits, price steps, etc.)

## 📊 Data Models & Response Formats

### Advertisement Object
```json
{
  "adId": "string",
  "cryptoCurrency": "string",
  "fiatCurrency": "string", 
  "side": "buy|sell",
  "amount": "string",
  "price": "string",
  "minOrderLimit": "string",
  "maxOrderLimit": "string",
  "paymentMethodIds": ["string"],
  "message": "string",
  "isPublic": true,
  "createdTimestamp": "string",
  "status": "active|paused|completed|cancelled"
}
```

### Order Object
```json
{
  "orderId": "string",
  "adId": "string", 
  "side": "buy|sell",
  "amount": "string",
  "price": "string",
  "status": "pending|paid|released|cancelled|disputed",
  "createdTimestamp": "string",
  "expireTime": "string",
  "payTimeLimit": 30,
  "counterpartyNickName": "string",
  "counterpartyUserId": "string"
}
```

### Message Object (Chat/Dispute)
```json
{
  "messageId": "string",
  "content": "string",
  "contentType": 101,
  "contentUrl": "string", 
  "isSentBySelf": true,
  "sentTimestamp": "string",
  "lastMessageSequence": "string"
}
```

## 🔐 Authentication & Security

All API endpoints require authentication via OKX API keys:
- **API-KEY**: Your OKX API key
- **SIGN**: Request signature (HMAC-SHA256)
- **TIMESTAMP**: Request timestamp
- **PASSPHRASE**: Your API passphrase

See [OKX API Documentation](https://www.okx.com/docs-v5) for authentication details.

## 💡 Best Practices & Common Patterns

### 1. Ad Creation Workflow
1. Create advertisement with appropriate pricing and limits
2. Monitor for incoming orders via webhooks or polling
3. Communicate with counterparty via chat system
4. Confirm payment received
5. Release cryptocurrency to complete trade

### 2. Dispute Handling
- Always attempt to resolve via chat first
- Gather evidence (payment proof, communication logs)
- File dispute within allowed timeframe
- Respond promptly to dispute messages
- Accept resolution if evidence supports counterparty claim

### 3. Security Measures
- Implement rate limiting (API has rate limits)
- Validate and sanitize all user inputs
- Use HTTPS for all API calls
- Store API credentials securely
- Implement proper error handling and retry logic

### 4. Payment Verification
- Verify payment receipts match order amount
- Check payment method matches ad requirements
- Confirm funds are in your account before releasing crypto
- Use escrow protection for high-value trades

### 5. User Management
- Maintain blacklist for problematic users
- Check user verification levels before trading
- Review completion rates and cancellation history
- Consider trade limits based on user reputation

## ⚠️ Important Notes

1. **Order Expiry**: Orders have expiration times - monitor and act within time limits
2. **Payment Windows**: Buyers have limited time to make payment after order creation
3. **Dispute Timeframes**: Disputes must be filed within specific windows after order creation
4. **Rate Limits**: API has rate limits - implement proper backoff and retry mechanisms
5. **Regulatory Compliance**: Ensure compliance with local KYC/AML regulations
6. **Market Volatility**: Consider price protection mechanisms for volatile markets
7. **Fraud Prevention**: Always verify payment authenticity before releasing crypto

## 📋 Reference Files

- [`references/OKX-P2P.md`](references/OKX-P2P.md) - Complete API reference (86 pages)
- [`references/index.md`](references/index.md) - Documentation index

## 🔧 Configuration & Setup

To use this skill effectively:

1. **API Credentials**: Obtain API key, secret, and passphrase from OKX
2. **Environment Setup**: Configure secure storage for credentials
3. **Rate Limiting**: Implement client-side rate limiting (20 requests/second recommended)
4. **Webhooks**: Consider setting up webhooks for real-time notifications
5. **Testing**: Use OKX testnet for development and testing

## 📈 Rate Limits & Limitations

- **General Limit**: 20 requests per second per IP
- **Burst Limit**: Burst capacity available for short periods
- **Weight System**: Different endpoints have different weights
- **IP Bans**: Excessive requests may result in temporary IP bans
- **Account Limits**: Some endpoints have per-account limits

## 🔄 Error Handling

Common error responses include:
- **Parameter Errors**: Missing or invalid parameters (400)
- **Authentication Errors**: Invalid credentials or signature (401)
- **Rate Limit Errors**: Too many requests (429)
- **Server Errors**: Internal server issues (500)
- **Business Logic Errors**: Invalid operations for current state (400 with error code)

Always check response codes and implement appropriate retry logic with exponential backoff.

---
*Generated from OKX P2P API Documentation (86 pages)*
*Skill Version: 1.0.0 | Quality Score: 95/100*
