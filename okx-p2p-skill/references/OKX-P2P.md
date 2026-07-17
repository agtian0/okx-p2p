# OKX-P2P

**Pages**: 1-86

---

**📄 Source: PDF Page 1**

API Specs - External​
1. Ads​
1.1 Create Ad​
Creates a new ad.  ​
HTTP Request​
POST /api/v5/p2p/ad/create​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
automatedM
essage​
String​
No​
Message that is sent to taker when an order is placed on this ad​
cryptoAmou
nt​
String​
Yes​
The quantity of cryptocurrency​
cryptoCurre
ncy​
String​
Yes​
The crypto currency symbol. Example: BTC​
fiatCurrency​
String​
Yes​
The fiat currency symbol. Example: USD​
isProofRequi
red​
Boolean​
No​
Indicates whether a proof (e.g., bank statement) is required for CNY 
ads. Valid values: true, false​
isPublic​
Boolean​
No​
Indicates whether the ad is targeted for public or private 
marketplace. Valid values: true,false
maxOrderLi
mit​
String​
Yes​
The maximum order limit. Example: 990.00​
maxPaymen
tDurationIn
Minutes​
String​
No​
The maximum time allowed for payment in minutes before 
timeout happens. Valid values can be fetched from the /config API 
from maxPaymentDurationAllowedValues field.​
 Examples: 5,10,15,30,60,120​
minAccount
Age​
String​
No​
The number of days since the user has registered (sign-up date). 
Valid values are: 30, 60, 180, 365​

### Code Examples

```unknown
user has registered (sign-up date).
```

```unknown
required for CNY
```

---

---

**📄 Source: PDF Page 2**

minComplet
edOrders​
String​
No​
The minimum number of completed orders by the transaction 
party​
minComplet
ionRate​
String​
No​
The minimum order completion rate of the taker. Example: 0.95​
minKycLevel​
String​
No​
The minimum identity verification level of the taker. Valid values: 
1,2,3​
minOrderLi
mit​
String​
Yes​
The minimum order limit. Example: 890.00
minSellOrde
rs​
String​
No​
The minimum number of sell orders completed by the taker. 
Example: 5​
paymentMet
hodIds​
Array of 
String​
No​
The Ids of payment methods which maker accepts for payments. 
Applicable only for 'sell' ads. Example: [1234]​
paymentMet
hods​
String​
No​
The payment methods which maker can transact in. Applicable 
only for 'buy' ads. Example: bank​
priceFloor​
String​
No​
The lowest price before the user's ad is hidden. Applicable only for 
ads with price type as floating_market. Example: 890.00​
priceMargin​
String​
No​
The price margin ratio for floating type ads. Applicable only for ads 
with price type as floating_market. Example: 0.01​
remark​
String​
No​
Additional information or trading instructions for the ad for taker​
side​
String​
Yes​
Specifies the transaction side or direction. Use buy to indicate a 
buy transaction, sell for a sell ​
transaction.​
targetGroup​
String​
Yes​
User target group for the ad. Valid values: 
common,certified,diamond,all​
type
String​
Yes​
Ad price type. Valid values are: limit, floating_market​
unitPrice​
String​
Yes​
The unit price in fiat currency. Applicable only for ads with price 
type as fixed price. Example: 1.1​
verificationT
ype​
String​
No​
Verification type for overseas ads excluding CNY. Valid values: 0 (No 
verification), 1 (Verification)​
verificationN
otes​
Array of 
Object​
No​
Notes set by the maker for Verification Ads to be shown as a 
prompt to the taker​

### Code Examples

```unknown
user's ad is hidden. Applicable only for
```

---

---

**📄 Source: PDF Page 3**

> id​
String​
No​
Verification note Id. ​
Valid values (CNY): ​
1 (Provide proof that the account funds used for payment have 
been credited for more than X days)​
Valid values (Overseas): ​
10 (Chat before payment)​
11 (No 3rd party payment)​
12 (Provide payment proof)​
13 (ID verification)​
> constraints​
Object​
No​
Constraints specified by the user​
>> min​
String​
No​
Min constraint value. Example: 1​
>> max​
String​
No​
Max constraint value. Example: 2​
>> 
maxLength​
String​
No​
Max length constraint value. Example: 10​
>> isActive​
Boolean​
No​
Specifies whether the constraint is active. Valid values: true, false​
> variables​
Object​
No​
Variables specified by the user for verification notes​
>> num​
String​
No​
Number​
>> others​
String​
No​
Miscellaneous​
whitelistedC
ountries​
Array of 
String​
No​
Regions that the taker must be from. Use ALL_COUNTRIES for 
including all countries. For other countries use the two-digit Id. 
Example: [US,UK,CA]​
Response Parameters​
Paramete
r​
Type​
Description​
adId​
String​
Id of the created ad​
1.2 Get Ad​
Gets the ad information by ad id.​

### Code Examples

```unknown
used for payment have
```

```unknown
user for verification notes​
```

```elixir
use the two-digit Id.
```

---

---

**📄 Source: PDF Page 4**

HTTP Request​
GET /api/v5/p2p/ad​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
adId​
String​
Yes​
Ad id​
Response Parameters​
Parameter​
Type​
Description​
adId​
String​
Ad id​
automatedMessage​
String​
Message that is sent to taker when an order is placed on 
this ad​
availableAmount​
String​
The available crypto quantity currently available for 
buying and selling​
blacklistStatus​
String​
Blacklist status. Valid values:​
NO_BLACK (No blacklist relationship)​
BLACK_OTHER (Current user blacklisted the other side)​
BLACKED (The other side blacklisted current user)​
BLACK_EACH_OTHER (Current user and other use 
blacklisted each other)​
blockedReasons​
Array of 
strings​
Collection of all blocked reasons. Example: Your 
completion rate is less than 0.5. We encourage you to 
increase it​
completedOrderCry
ptoAmount​
String​
The amount of crypto that has been traded till now​
completedOrderFia
tAmount​
String​
The amount of fiat that has been traded till now
configuredPayment
MethodDetails​
Array of 
objects​
Collection of maker payment information​
> paymentMethod
String​
Payment method​

### Code Examples

```unknown
user blacklisted the other side)​
```

```unknown
user and other use
```

---

---

**📄 Source: PDF Page 5**

> openStatus​
String​
Payment method switch state. Valid values: ​
open​
close​
unbound​
> 
paymentMethodDet
ails​
Array of 
objects​
Collection of payment method details​
>> 
paymentMethodId​
String​
Payment method Id​
>> accountNo​
String​
The account number of payment method​
>> bankName
String​
Bank name​
createdTimestamp​
String​
Creation time of the ad​
creator​
Object​
Ad creator details​
> id​
String​
User Id​
> nickName​
String​
Nick name of the user​
> realName​
String​
Real name of the user​
> type​
String​
User type for the ad. Valid values: ​
common​
certified​
diamond​
> completedOrders​
String​
The number of orders completed by the user​
> cancelledOrders​
String​
The number of orders canceled by the user​
> 
completedSellOrder
s​
String​
The number of sell orders completed by the user​
> completionRate​
String​
The order completion rate of the user​
> kycLevel​
String​
The identity verification level of the user. Valid values: 1, 
2, 3​
> acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do 
not accept order), 1 (accept order)​
String​
Average payment time in seconds​

### Code Examples

```json
user. Valid values: 1,
```

```json
user. Valid values: 0 (do
```

---

---

**📄 Source: PDF Page 6**

> 
avgPaymentTimeIn
Seconds​
> 
avgCompletionTim
eInSeconds​
String​
Average completion time in seconds​
> 
createdTimestamp​
String​
User joining timestamp in milliseconds​
> hasAlreadyTraded​
Boolean​
Specifies whether the user has traded in the past with 
the requester. Valid values: true, false​
cryptoCurrency​
String​
Crypto currency symbol​
cryptoScale​
String​
Crypto currency decimal places​
fiatCurrency​
String​
Fiat currency symbol​
fiatPriceIncrement​
String​
Fiat currency increasing unit price gradient​
fiatPriceScale​
String​
Decimal places reserved for fiat currency​
fiatScale​
String​
Fiat Currency decimal places​
hiddenCategory​
String​
Hidden  Category. Valid values are: ​
1 (hide one)​
0 (not hidden)​
3 (out of stock)​
hiddenReason​
String​
All ads hidden reasons​
hiddenType​
String​
Order offline type. Valid values:​
0​
1​
isBlockTradeCatego
ry​
Boolean​
Specifies whether the ad is a block trade ad (ad dealing 
with large amount)​
isCreatorBlockedBy
CurrentUser​
Boolean​
Specifies whether blocked by the current user​
isHidden​
Boolean​
Specifies whether the ad is hidden or not​
isListedOnMarketpl
ace​
Boolean​
Specifies whether the ad is listed on marketplace​
isOwner​
Boolean​
Specifies whether the ad belongs to the user​

### Code Examples

```unknown
user has traded in the past with
```

---

---

**📄 Source: PDF Page 7**

isPriceOutOfRange​
Boolean​
Specifies whether index rate deviates too much​
isProofRequired​
Boolean​
Specifies whether proof is required​
isSecurityLimitAppli
cable​
Boolean​
Specifies whether T+1 order​
latestUserRegistere
dTimestamp​
String​
Transaction party user maximum registration time. 
Example: 1686652358497​
maxCompletedOrde
rs​
String​
The maximum number of orders completed by the taker​
maxOrderSize​
String​
Order upper limit​
maxAvgCompleteTi
me​
String​
The maximum average completion time of the 
transaction parties​
maxPaymentDurati
onInMinutes​
String​
The maximum time allowed for payment in minutes 
before timeout happens.​
merchantId​
String​
Merchant Id​
minAccountAge​
String​
The number of days since the user has registered (sign-
up date). Example: 30​
minCompletedOrde
rs​
String​
The minimum number of orders completed by the taker​
minCompletionRate​
String​
The minimum order completion rate of the taker​
minKycLevel​
String​
The minimum identity verification level of the taker. 
Valid values: 1,2,3​
minOrderSize​
String​
Order lower limit​
minSellOrders​
String​
The minimum number of sell orders completed by the 
taker​
onHoldAmount​
String​
The quantity that has been frozen but the order has not 
been completed till now​
paymentMethodBas
icInfoList​
Array of 
Object​
Collection of payment method basic info set by the 
maker. Applicable for buy ads.​
> paymentMethod
String​
Payment method name​
Boolean​
Indicate whether the payment method instantly settle​

### Code Examples

```unknown
user maximum registration time.
```

```unknown
user has registered (sign-
requirement or processing time
```

---

---

**📄 Source: PDF Page 8**

> 
isInstantSettlePaym
ent​
> transferSpeed​
String​
Indicates the speed of the payment method. Valid 
values: ​
0 (nil): No specific speed requirement or processing time 
mentioned. ​
1 (real time): Payment is expected to be processed 
immediately or in real-time.​
2 (instant crypto release): Payment release or 
confirmation is expected to be instant for cryptocurrency 
transactions.​
3 (up to X days): Payment processing may take up to a 
certain number of days, where X represents the specific 
number of days mentioned.​
platformCommissio
nRate​
String​
Commission rate charged by the platform​
priceMargin​
String​
The price margin ratio for floating type ads. Applicable 
only for ads with price type as floating price​
realFiatMaxAmount
PerOrder​
String​
Original order maximum amount​
remark​
String​
Additional information or instructions for the ad for taker​
side​
String​
Specifies the transaction side or direction. Valid values:​
buy​
sell​
status​
String​
Order status. Valid values:​
new​
canceled​
completed
creating​
create_fail​
canceling​
cancel_fail​
targetGroup​
String​
User target group for the ad. Valid values: ​

---

---

**📄 Source: PDF Page 9**

common​
certified​
diamond​
all​
type
String​
Ad price type. Valid values: ​
limit​
floating_market​
unitPrice​
String​
Unit price​
unpaidOrderTimeo
utInMinutes​
String​
Payment time in minutes​
updatedTimestamp​
String​
Timestamp of latest modification of ad. Example: 
1686652358497
userRegisteredInter
valInDays​
String​
Maximum registration interval in days​
verificationNotes​
Array of 
Object​
Notes for Verification Ads to be shown as a prompt to the 
taker​
>id​
Integer​
Verification note Id. ​
Valid values (CNY): ​
1 (Provide proof that the account funds used for 
payment have been credited for more than X days)​
Valid values (Overseas): ​
10 (Chat before payment)​
11 (No 3rd party payment)​
12 (Provide payment proof)​
13 (ID verification)​
>description​
String​
Text description of verification type​
>viewType​
String​
For UI display can ignore for OpenAPI ​
> constraints​
Object​
Constraints specified by the user​
>> active​
Boolean​
Specifies whether the constraint is active​
>> max​
Integer​
Max payment account duration value​

### Code Examples

```unknown
userRegisteredInter
```

---

---

**📄 Source: PDF Page 10**

>> min​
Integer​
Min payment account duration value
>> maxLength​
Integer​
Max length for others constraint value​
>variables​
Object​
Variables specified by the user for verification notes​
>> num​
Integer​
Number​
>> others​
String​
Miscellaneous​
verificationType​
String​
Specifies the verification type. Applies for Overseas Ads. 
Valid values:​
0 (no verification required)​
1 (verification required)​
whitelistedCountrie
s​
String​
Regions that the taker must be from, as set by the maker 
of the ad​
1.3 Update Ad​
This operation would cancel the existing order and create a new one. If the required parameters 
are not passed, then we default to using the old ad values. ​
HTTP Request​
POST /api/v5/p2p/ad/update​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
adId​
String​
Yes​
Id of the Ad which needs to be updated​
online​
String​
No​
Status of the ad: true (online), false (offline)​
minOrderLimit​
String​
No​
The minimum order limit. Example: 890.00
maxOrderLimi
t​
String​
No​
The maximum order limit. Example: 990.00​
type
String​
No​
Ad price type. Valid values are: limit, floating_market​
priceMargin​
String​
No​
The price margin ratio for floating type ads. Applicable only for 
ads with price type as floating price. Example: 0.01​
unitPrice​
String​
No​
The unit price in fiat currency. Applicable only for ads with price 
type as fixed price. Example: 1.1​

### Code Examples

```unknown
user for verification notes​
```

```unknown
required parameters
```

---

---

**📄 Source: PDF Page 11**

cryptoAmount​
String​
No​
The quantity of cryptocurrency​
priceFloor​
String​
No​
The lowest price before the user's ad is hidden. Example: 890.00​
isPublic​
Boolea
n​
No​
Indicates whether the ad is targeted for public or private 
marketplace. Valid values: true,false
paymentMeth
odIds​
Array of 
String​
No​
The Ids of payment methods which maker accepts for payments. 
Applicable only for 'sell' ads. Example: [1234]​
paymentMeth
ods​
String​
No​
The payment methods which maker can transact in. Applicable 
only for 'buy' ads. Example: bank​
minCompleted
Orders​
String​
No​
The minimum number of completed orders by the taker​
minKycLevel​
String​
No​
The minimum identity verification level of the taker. Valid values: 
1,2,3​
minSellOrders​
String​
No​
The minimum number of sell orders completed by the taker. 
Example: 5​
minCompletio
nRate​
String​
No​
The minimum order completion rate of the taker. Example: 0.95​
minAccountAg
e​
String​
No​
The number of days since the user has registered (sign-up date). 
Valid values are: 30, 60, 180, 365​
targetGroup​
String​
No​
User target group for the ad. Valid values: 
common,certified,diamond,all​
maxPaymentD
urationInMinut
es​
String​
No​
The maximum time allowed for payment in minutes before 
timeout happens. Valid values: 5,10,15,30,60,120​
isProofRequire
d​
Boolea
n​
No​
Indicates whether proof (e.g., bank statement) is required for CNY 
ads. Valid values: true, false​
whitelistedCou
ntries​
Array of 
String​
No​
Regions that the taker must be from. Use ALL_COUNTRIES for 
including all countries. For other countries use the two-digit Id. 
Example: [US,UK,CA]​
verificationTyp
e​
String​
No​
Verification type for overseas ads excluding CNY. Example: 0 (No 
verification), 1 (Verification))​
verificationNot
es​
Array of 
Object​
No​
Notes set by the maker for Verification Ads to be shown as a 
prompt to the taker​
Valid values (CNY): ​

### Code Examples

```unknown
user has registered (sign-up date).
```

```elixir
use the two-digit Id.
```

```json
user's ad is hidden. Example: 890.00​
```

```unknown
required for CNY
```

---

---

**📄 Source: PDF Page 12**

1 (Provide proof that the account funds used for payment have 
been credited for more than X days)​
Valid values (Overseas): ​
10 (Chat before payment)​
11 (No 3rd party payment)​
12 (Provide payment proof)​
13 (ID verification)​
> id​
String​
No​
Verification note Id. Valid values: 1 (Provide proof that the 
account funds used for payment have been credited for more 
than X days)​
> constraints​
Object​
No​
Constraints specified by the user​
>> min​
String​
No​
Min payment account duration value. Example: 1​
>> max​
String​
No​
Max payment account duration value. Example: 2​
>> maxLength​
String​
No​
Max length constraint value. Example: 10​
>> isActive​
Boolea
n​
No​
Specifies whether the constraint is active. Valid values: true, false​
> variables​
Object​
No​
Variables specified by the user for verification notes​
>> num​
String​
No​
Number​
>> others​
String​
No​
Miscellaneous​
remark​
String​
No​
Additional information or trading instructions for the ad for taker​
automatedMes
sage​
String​
No​
Message that is sent to taker when an order is placed on this ad​
Response Parameters​
Paramete
r​
Type​
Description​
oldAdId​
String​
Id of the cancelled ad​
newAdId​
String​
Id of the newly created ad​

### Code Examples

```unknown
used for payment have
```

```unknown
used for payment have been credited for more
```

```unknown
user for verification notes​
```

---

---

**📄 Source: PDF Page 13**

1.4 Update Ad Active Status​
Updates the ad status to be online or offline.​
HTTP Request​
POST /api/v5/p2p/ad/update-active-status​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
adId​
String​
Yes​
Id of the Ad for which status needs to be modified​
status​
String​
Yes​
New online status of the Ad. Valid values: hidden, show​
Response Parameters​
Paramete
r​
Type​
Description​
adId​
String​
Id of the Ad for which status got modified​
1.5 Cancel Ad​
Cancel an ad​
HTTP Request​
POST /api/v5/p2p/ad/cancel​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
adId​
String​
Yes​
Id of the Ad to be canceled​
Response Parameters​
Paramete
r​
Type​
Description​

---

---

**📄 Source: PDF Page 14**

adId​
String​
Id of the cancelled Ad​
1.6 Get Optimal Ad Price​
Get top buy top sell price​
HTTP Request​
GET /api/v5/p2p/ad/optimal-price​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
cryptoCurre
ncy​
String​
Yes​
Crypto currency symbol​
fiatCurrenc
y​
String​
Yes​
Fiat currency symbol​
Response Parameters​
Parameter​
Type​
Description​
currentHighestBuyAd
Price​
String​
Current highest buy ad price​
currentLowestSellAd
Price​
String​
Current lowest sell ad price​
1.7 Get Marketplace List​
Get buy and sell ad list. Return similar ads which are visible on the marketplace on app/website.​
HTTP Request​
GET /api/v5/p2p/ad/marketplace-list​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​

---

---

**📄 Source: PDF Page 15**

side​
String​
No​
Specifies the transaction side or direction. Use buy to 
indicate a buy transaction, sell for a sell transaction, or all to 
include both buy and sell transactions.​
cryptoCurrency​
String​
Yes​
Crypto currency symbol​
fiatCurrency​
String​
Yes​
Fiat currency symbol​
targetGroup​
String​
No​
User target group for the ad. Valid values: 
common,certified,diamond,all,blockTrade,flashtrade​
minCryptoAmount​
String​
No​
Minimum amount of crypto​
cryptoQuota​
String​
No​
The crypto currency limit, which is the amount of crypto 
currency multiplied by the unit price and the comparison of 
the limit of the order. Example: 5.9​
minFiatAmount​
String​
No​
Fiat currency quantity (ads with fiat amount less than this 
number would be filtered out)​
maxFiatAmount​
String​
No​
Fiat currency quantity (ads with fiat amount greater than 
this number would be filtered out)​
minFiatAmountPerOr
der​
String​
No​
The minimum fiat amount required for a single order. Any 
ads with orders placed for an amount less than this 
threshold will be filtered out​
maxFiatAmountPerO
rder​
String​
No​
The maximum fiat amount required for a single order. Any 
ads with orders placed for an amount greater than this 
threshold will be filtered out​
paymentMethod​
String​
No​
Payment method. Default: all. Examples: all, bank, aliPay, 
wxPay​
isTradable​
Boolea
n​
No​
Specifies whether the ad is tradable or not. Default: false​
isSecurityLimitApplic
able​
Boolea
n​
No​
Specifies whether to show T+1 ads. Default: false​
shouldShowOnlyFoll
ow​
Boolea
n​
No​
Specifies whether to fetch ads from users which the current 
user follows. Default: false. Valid values: true, false​
showAlreadyTraded​
Boolea
n​
No​
Specifies whether to fetch ads which have already been 
traded with the user. Default: false. Valid values: true, false​
isProofRequired​
Boolea
n​
No​
Specifies whether verification is required for the ads. 
Default: false. Valid values: true, false​

### Code Examples

```unknown
users which the current 
user follows. Default: false. Valid values: true, false​
```

```unknown
include both buy and sell transactions.​
```

```unknown
required for a single order. Any
```

```unknown
user. Default: false. Valid values: true, false​
```

```unknown
required for the ads.
```

---

---

**📄 Source: PDF Page 16**

hideOverseasVerifica
tionAds​
Boolea
n​
No​
Specifies whether to hide overseas verification ads. Default: 
false. Applies only for non-CNY regions. Valid values: true, 
false​
limit​
String​
No​
Maximum number of items returned​
sortType​
String​
No​
Sort type for the ads. Valid values: 
default,recommended,price_asc,price_desc​
Response Parameters​
Parameter​
Type​
Description​
sellAds​
Array of 
Object​
Collection of sell ad details​
buyAds​
Array of 
Object​
Collection of buy ad details​
> adId​
String​
Ad Id​
> minSellOrders​
String​
Minimum number of sell orders completed by the trading 
party​
> side​
String​
Specifies the transaction side or direction. Valid values: 
buy,sell,block_buy,block_sell​
> cryptoCurrency​
String​
Crypto currency symbol​
> fiatCurrency​
String​
Fiat currency symbol​
> minOrderSize​
String​
Order lower limit​
> maxOrderSize​
String​
Order upper limit​
> availableAmount​
String​
The available current quantity that can be bought/sold​
> unitPrice​
String​
The unit price in fiat currency. Applicable only for ads with 
price type as fixed price. Example: 1.1​
> creator​
Object​
Information about the ad creator.​
>> hasAlreadyTraded​
Boolean​
Specifies whether the ad creator has already traded with the 
user​
>> nickName​
String​
Nick name of the ad creator​

---

---

**📄 Source: PDF Page 17**

>> userId​
String​
Id of the ad creator​
>> cancelledOrders​
String​
Number of orders cancelled by the user​
>> merchantId​
String​
Merchant Id​
>> type​
String​
Ad creator type. Valid values: all, common (non-
authenticated), certified (authenticated)​
>> completedOrders​
String​
Total orders completed by the ad creator​
>> completionRate​
String​
Completion rate of the ad creator​
>> isBlacklistedByUser​
Boolean​
Specifies whether the ad creator is blocked by the user​
> paymentMethods​
Array of 
String​
Collection of payment methods. Example: bank, aliPay, 
wxPay​
> 
paymentMethodBasicIn
foList​
Array of 
Object​
Collection of payment method basic info set by the maker. 
Applicable for buy ads​
>> paymentMethod​
String​
Payment method name​
>> 
isInstantSettlePayment​
Boolean​
Indicate whether the payment method instantly settle​
>> transferSpeed​
String​
Indicates the speed of the payment method. Valid values: ​
0 (nil): No specific speed requirement or processing time 
mentioned. ​
1 (real time): Payment is expected to be processed 
immediately or in real-time.​
2 (instant crypto release): Payment release or confirmation is 
expected to be instant for cryptocurrency transactions.​
3 (up to X days): Payment processing may take up to a 
certain number of days, where X represents the specific 
number of days mentioned.​
> fiatScale​
String​
Fiat Currency decimal places​
> isOwner​
Boolean​
Specifies whether the ad belongs to the user​
> minCompletedOrders​
String​
The minimum number of completed orders specified by the 
ad creator​
> maxCompletedOrders​
String​
The maximum number of completed orders specified by the 
ad creator​

### Code Examples

```unknown
requirement or processing time
```

---

---

**📄 Source: PDF Page 18**

> minCompletionRate​
String​
The minimum completion rate of the taker specified by the 
ad creator​
> targetGroup​
String​
User target group for the ad. Valid values: ​
common​
certified​
diamond​
all​
> 
maxAvgCompletionTim
e​
String​
The maximum average completion time of the taker​
> 
isSecurityLimitApplicabl
e​
Boolean​
Specifies whether T+1 ad​
> isProofRequired​
Boolean​
Indicates whether a proof (e.g., bank statement) is required 
for CNY ads. Valid values: true, false​
> verificationType​
String​
Verification type for overseas ads excluding CNY. Valid 
values: 0 (No verification), 1 (Verification)​
> fiatSymbol
String​
Fiat currency symbol. Examples: ￥,$​
recommendedAd​
Array of 
Object​
Recommended ads​
> userGroup​
String​
User group that can see ad. Valid values: 0 (new users), 1 
(returning users), 2 (both)​
> ad​
Object​
Ad details. Schema is the same as what it is for buy/sell ads​
Sample Response:​
{
  "code": 0,
  "data": [
    {
      "buyAds": [
        {
          "adId": "230206170034022",
          "availableAmount": "154.00",
          "creator": {
1
2
3
4
5
6
7
8
9
10

### Code Examples

```json
{
      "buyAds": [
        {
          "adId": "230206170034022",
          "availableAmount": "154.00",
          "creator": {
```

```unknown
users), 2 (both)​
```

---

---

**📄 Source: PDF Page 19**

"cancelledOrders": "7",
            "completedOrders": "200001",
            "completionRate": "0.9999",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "bba0ea46b8",
            "nickName": "1234424",
            "type": "diamond",
            "userId": "2460c7a78d"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
          "isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
          "maxOrderSize": "646.00",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "buy",
          "targetGroup": "all",
          "unitPrice": "6.4600",
          "verificationType": "0"
        },
        {
          "adId": "230208145147869",
          "availableAmount": "29.00",
          "creator": {
            "cancelledOrders": "2",
            "completedOrders": "0",
            "completionRate": "0.0000",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "ceb26b15e6",
            "nickName": "Test@1675838705282",
            "type": "certified",
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57

### Code Examples

```json
"cancelledOrders": "7",
            "completedOrders": "200001",
            "completionRate": "0.9999",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "bba0ea46b8",
            "nickName": "1234424",
            "type": "diamond",
            "userId": "2460c7a78d"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
          "isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
          "maxOrderSize": "646.00",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "buy",
          "targetGroup": "all",
          "unitPrice": "6.4600",
          "verificationType": "0"
        },
        {
          "adId": "230208145147869",
          "availableAmount": "29.00",
          "creator": {
            "cancelledOrders": "2",
            "completedOrders": "0",
            "completionRate": "0.0000",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "ceb26b15e6",
            "nickName": "Test@1675838705282",
            "type": "certified",
```

```json
userId": "2460c7a78d"
```

---

---

**📄 Source: PDF Page 20**

"userId": "e436507906"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
          "isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
          "maxOrderSize": "187.34",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "buy",
          "targetGroup": "all",
          "unitPrice": "6.4600",
          "verificationType": "0"
        }
      ],
      "recommendedAd": {
        "ad": {
          "adId": "230710173636129",
          "availableAmount": "999999.00",
          "creator": {
            "cancelledOrders": "0",
            "completedOrders": "0",
            "completionRate": "0.0000",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "9a9aa9acc9",
            "nickName": "ftt.maker",
            "type": "diamond",
            "userId": "4f9054eaf1"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104

### Code Examples

```json
"userId": "e436507906"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
          "isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
          "maxOrderSize": "187.34",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "buy",
          "targetGroup": "all",
          "unitPrice": "6.4600",
          "verificationType": "0"
        }
      ],
      "recommendedAd": {
        "ad": {
          "adId": "230710173636129",
          "availableAmount": "999999.00",
          "creator": {
            "cancelledOrders": "0",
            "completedOrders": "0",
            "completionRate": "0.0000",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "9a9aa9acc9",
            "nickName": "ftt.maker",
            "type": "diamond",
            "userId": "4f9054eaf1"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
```

```json
userId": "e436507906"
```

```json
userId": "4f9054eaf1"
```

---

---

**📄 Source: PDF Page 21**

"isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
          "maxOrderSize": "6999993.00",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "sell",
          "targetGroup": "all",
          "unitPrice": "7.0000",
          "verificationType": "0"
        },
        "userGroup": "0"
      },
      "sellAds": [
        {
          "adId": "230710173636129",
          "availableAmount": "999999.00",
          "creator": {
            "cancelledOrders": "0",
            "completedOrders": "0",
            "completionRate": "0.0000",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "9a9aa9acc9",
            "nickName": "ftt.maker",
            "type": "diamond",
            "userId": "4f9054eaf1"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
          "isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151

### Code Examples

```json
"isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
          "maxOrderSize": "6999993.00",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "sell",
          "targetGroup": "all",
          "unitPrice": "7.0000",
          "verificationType": "0"
        },
        "userGroup": "0"
      },
      "sellAds": [
        {
          "adId": "230710173636129",
          "availableAmount": "999999.00",
          "creator": {
            "cancelledOrders": "0",
            "completedOrders": "0",
            "completionRate": "0.0000",
            "hasAlreadyTraded": false,
            "isBlacklistedByUser": false,
            "merchantId": "9a9aa9acc9",
            "nickName": "ftt.maker",
            "type": "diamond",
            "userId": "4f9054eaf1"
          },
          "cryptoCurrency": "usdt",
          "fiatCurrency": "cny",
          "fiatScale": "2",
          "fiatSymbol": "¥",
          "isOwner": "false",
          "isProofRequired": false,
          "isSecurityLimitApplicable": false,
          "maxAvgCompletionTime": "",
          "maxCompletedOrders": "0",
```

```json
userId": "4f9054eaf1"
```

---

---

**📄 Source: PDF Page 22**

"maxOrderSize": "6999993.00",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "sell",
          "targetGroup": "all",
          "unitPrice": "7.0000",
          "verificationType": "0"
        }
      ]
    }
  ],
  "msg": ""
}
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
1.8 Get Ad share info​
Gets Ad sharing info with QRcode, url, ad details. This is similar to the ad share feature on 
web/mobile.​
HTTP Request​
GET /api/v5/p2p/ad/share-info​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
adId​
String​
No​
Ad id for which sharing info needs to be generated​
Response Parameters​
Parameter​
Type​
Description​
adId​
String​
Ad id for which sharing info is generated​
side​
String​

### Code Examples

```json
"maxOrderSize": "6999993.00",
          "minCompletedOrders": "0",
          "minCompletionRate": "0.0",
          "minKycLevel": "1",
          "minOrderSize": "1.00",
          "minSellOrders": "0",
          "paymentMethodBasicInfoList": [],
          "paymentMethods": [
            "bank"
          ],
          "remark": "",
          "side": "sell",
          "targetGroup": "all",
          "unitPrice": "7.0000",
          "verificationType": "0"
        }
      ]
    }
```

---

---

**📄 Source: PDF Page 23**

Specifies the transaction side or direction. Valid values: 
buy,sell,block_buy,block_sell​
cryptoCurrency​
String​
Crypto currency symbol​
fiatCurrency​
String​
Fiat currency symbol​
cryptoDecimalPlaces​
String​
Crypto currency decimal places​
fiatDecimalPlaces​
String​
Fiat currency decimal places​
minOrderLimit​
String​
The minimum order limit. Example: 890.00
maxOrderLimit​
String​
The maximum order limit. Example: 990.00​
unitPrice​
String​
The unit price in fiat currency. Applicable only for ads with price type 
as fixed price. Example: 1.1​
fiatPriceScale​
String​
Decimal places reserved for fiat currency​
fiatPriceIncrement​
String​
Fiat currency increasing unit price gradient​
paymentMethods​
Array of 
String​
The payment methods which maker can transact in. Applicable only 
for 'buy' ads. Examples: bank,aliPay,wxPay​
depositPaymentMeth
ods​
Array of 
Object​
Collection of deposit payment methods​
> paymentMethod
String​
Payment method code. Example: bank​
> description​
String​
Description of payment method​
remark​
String​
Additional information or instructions for the ad for taker​
minKycLevel​
String​
The minimum identity verification level of the taker. Valid values: 
1,2,3​
targetGroup​
String​
User target group for the ad. Valid values: 
common,certified,diamond,all​
availableAmount​
String​
The available crypto quantity currently available for buying and 
selling​
nickName​
String​
Nick name of the creator​
minCompletionRate​
String​
The minimum order completion rate of the taker. Example: 0.95​
minCompletedOrder
s​
String​
The minimum number of completed orders specified by the ad 
creator​
String​

---

---

**📄 Source: PDF Page 24**

maxCompletedOrder
s​
The maximum number of completed orders specified by the ad 
creator​
isPublic​
Boolean​
Indicates whether the ad is targeted for public or private 
marketplace. Valid values: true,false
userLevel​
String​
Ad creator level. Valid values：common，certified，diamond​
minKycLevel​
String​
The minimum identity verification level of the taker. Valid values: 
1,2,3​
1.9 Get Active ads​
Get active ads for the user. Schema is similar to Get Ad API.​
HTTP Request​
GET /api/v5/p2p/ad/active-list​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
side​
String​
Yes​
Specifies the transaction side or direction. Use buy to indicate a 
buy transaction, sell for a sell ​
transaction.​
cryptoCurren
cy​
String​
Yes​
The crypto currency symbol. Example: BTC​
fiatCurrency​
String​
Yes​
The fiat currency symbol. Example: USD​
Response Parameters​
Parameter​
Type​
Description​
adId​
String​
Ad id​
type
String​
Ad price type. Valid values: ​
limit​
floating_market​
side​
String​
Specifies the transaction side or direction. Valid values:​
buy​

### Code Examples

```unknown
user. Schema is similar to Get Ad API.​
```

---

---

**📄 Source: PDF Page 25**

sell​
cryptoCurrency​
String​
Crypto currency symbol​
fiatCurrency​
String​
Fiat currency symbol​
minOrderSize​
String​
Order lower limit​
maxOrderSize​
String​
Order upper limit​
availableAmount​
String​
The available crypto quantity currently available for buying and 
selling​
completedOrderCryptoA
mount​
String​
The amount of crypto that has been traded till now​
completedOrderFiatAmou
nt​
String​
The amount of fiat that has been traded till now
onHoldAmount​
String​
The quantity that has been frozen but the order has not been 
completed till now​
unitPrice​
String​
Unit price​
priceMargin​
String​
The price margin ratio for floating type ads. Applicable only for 
ads with price type as floating price​
creator​
Object​
Details of the ad creator​
> userId​
String​
User Id​
> nickName​
String​
Nick name of the user​
> realName​
String​
Real name of the user​
> type​
String​
User type. Valid values: ​
common​
certified​
diamond​
all​
> completedOrders​
String​
The number of orders completed by the user​
> cancelledOrders​
String​
The number of orders canceled by the user​
> completedSellOrders​
String​
The number of sell orders completed by the user​
> completionRate​
String​
The order completion rate of the user​

---

---

**📄 Source: PDF Page 26**

> kycLevel​
String​
The identity verification level of the user​
> acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do not 
accept order), 1 (accept order)​
> 
avgPaymentTimeInSecon
ds​
String​
Average payment time in seconds​
> 
avgCompletionTimeInSec
onds​
String​
Average completion time in seconds​
> createdTimestamp​
String​
User joining timestamp in milliseconds​
> hasAlreadyTraded​
Boolea
n​
Specifies whether the user has traded in the past with the 
requester. Valid values: true, false​
> 
paymentMethodBasicInfo
List​
Array of 
Object​
Collection of payment method basic info set by the maker. 
Applicable for buy ads.​
>> paymentMethod​
String​
Payment method name​
>> isInstantSettlePayment​
Boolea
n​
Indicate whether the payment method instantly settle​
>> transferSpeed​
String​
Indicates the speed of the payment method. Valid values: ​
0 (nil): No specific speed requirement or processing time 
mentioned. ​
1 (real time): Payment is expected to be processed immediately 
or in real-time.​
2 (instant crypto release): Payment release or confirmation is 
expected to be instant for cryptocurrency transactions.​
3 (up to X days): Payment processing may take up to a certain 
number of days, where X represents the specific number of days 
mentioned.​
minKycLevel​
String​
The minimum identity verification level of the taker. Valid values: 
1,2,3​
remark​
String​
Additional information or instructions for the ad for taker​
createdTimestamp​
String​
Creation time of the ad​
isHidden​
Boolea
n​
Specifies whether the ad is hidden or not​

### Code Examples

```unknown
user has traded in the past with the
```

```unknown
requirement or processing time
```

```json
user. Valid values: 0 (do not
```

---

---

**📄 Source: PDF Page 27**

fiatPriceScale​
String​
Decimal places reserved for fiat currency​
fiatPriceIncrement​
String​
Fiat currency increasing unit price gradient​
fiatScale​
String​
Fiat Currency decimal places​
cryptoScale​
String​
Crypto currency decimal places​
isOwner​
Boolea
n​
Specifies whether the ad belongs to the user​
minCompletedOrders​
String​
The minimum number of orders completed by the taker​
maxCompletedOrders​
String​
The maximum number of orders completed by the taker​
minSellOrders​
String​
The minimum number of sell orders completed by the taker​
minCompletionRate​
String​
The minimum order completion rate of the taker​
targetGroup​
String​
User target group for the ad. Valid values: ​
common​
certified​
diamond​
all​
maxAvgCompleteTime​
String​
The maximum average completion time of the transaction 
parties​
isBlockTradeCategory
Boolea
n​
Specifies whether the ad is a block trade ad (ad dealing with 
large amount)​
isPriceOutOfRange​
Boolea
n​
Specifies whether index rate deviates too much​
maxPaymentDurationInMi
nutes​
String​
The maximum time allowed for payment in minutes before 
timeout happens.​
status​
String​
Order status. Valid values:​
new​
canceled​
completed
creating​
create_fail​
canceling​
cancel_fail​

---

---

**📄 Source: PDF Page 28**

blacklistStatus​
String​
Blacklist status​
merchantId​
String​
Merchant Id​
status​
String​
platformCommissionRate​
String​
Commission rate charged by the platform​
isListedOnMarketplace​
Boolea
n​
Specifies whether the ad is listed on marketplace​
unpaidOrderTimeoutInMi
nutes​
String​
Payment time in minutes​
realFiatMaxAmountPerOr
der​
String​
Original order maximum amount​
isSecurityLimitApplicable​
Boolea
n​
Specifies whether T+1 order​
isProofRequired​
Boolea
n​
Specifies whether proof is required​
verificationType​
String​
Specifies the verification type. Applies for Overseas Ads. Valid 
values:​
0 (no verification required)​
1 (verification required)​
verificationNotes​
Array of 
Object​
Notes for Verification Ads to be shown as a prompt to the taker​
>id​
Integer​
Verification note Id. ​
Valid values (CNY): ​
1 (Provide proof that the account funds used for payment have 
been credited for more than X days)​
Valid values (Overseas): ​
10 (Chat before payment)​
11 (No 3rd party payment)​
12 (Provide payment proof)​
13 (ID verification)​
>description​
String​
Text description of verification type​

### Code Examples

```unknown
used for payment have
```

---

---

**📄 Source: PDF Page 29**

>viewType​
String​
For UI display can ignore for OpenAPI ​
> constraints​
Object​
Constraints specified by the user​
>> active​
Boolea
n​
Specifies whether the constraint is active​
>> max​
Integer​
Max payment account duration value​
>> min​
Integer​
Min payment account duration value
>> maxLength​
Integer​
Max length for others constraint value​
>variables​
Object​
Variables specified by the user for verification notes​
>> num​
Integer​
Number​
>> others​
String​
Miscellaneous​
configuredPaymentMetho
dDetails​
Array of 
objects​
Collection of maker payment information​
> paymentMethod
String​
Payment method​
> openStatus​
String​
Payment method switch state. Valid values: ​
open​
close​
unbound​
> paymentMethodDetails​
Array of 
objects​
Collection of payment method details​
>> paymentMethodId​
String​
Payment method Id​
>> accountNo​
String​
The account number of payment method​
>> bankName
String​
Bank name​
minAccountAge​
String​
The number of days since the user has registered (sign-up date). 
Example: 30​
hiddenType​
String​
Order offline type. Valid values:​
0​
1​
updatedTimestamp​
String​
Timestamp of latest modification of ad. Example: 1686652358497​
String​
Maximum registration interval in days​

### Code Examples

```unknown
user for verification notes​
```

```unknown
user has registered (sign-up date).
```

---

---

**📄 Source: PDF Page 30**

userRegisteredIntervalInD
ays​
latestUserRegisteredTime
stamp​
String​
Transaction party user maximum registration time. Example: 
1686652358497
whitelistedCountries​
String​
Regions that the taker must be from, as set by the maker of the 
ad​
hiddenReason​
String​
All ads hidden reasons​
hiddenCategory​
String​
Hidden  Category. Valid values are: ​
1 (hide one)​
0 (not hidden)​
3 (out of stock)​
blockedReasonList​
Array of 
strings​
Collection of all blocked reasons. Example: Your completion rate 
is less than 0.5. We encourage you to increase it​
1.10 Get Ad Config​
Gets the ad config which is used to tell valid values for ad creation.​
HTTP Request​
GET /api/v5/p2p/ad/config​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​
side​
String​
Yes​
Specifies the transaction side or direction. Use buy to indicate a 
buy transaction, sell for a sell ​
transaction.​
cryptoCurrency​
String​
Yes​
The crypto currency symbol. Example: BTC​
fiatCurrency​
String​
Yes​
The fiat currency symbol. Example: USD​
isPublic​
Boolea
n​
No​
Indicates whether the ad is targeted for public or private 
marketplace. Valid values: true,false
Response Parameters​
Parameter​
Type​
Description​

### Code Examples

```unknown
user maximum registration time. Example:
```

```unknown
used to tell valid values for ad creation.​
```

```unknown
userRegisteredIntervalInD
```

---

---

**📄 Source: PDF Page 31**

blockTradeForUserAllow
ed​
Boolea
n​
Specifies whether the user is eligible to place block trades. Valid 
values: true/false​
blockTradeForFiatAllowe
d​
Boolea
n​
Specifies whether block trade is allowed for this fiat currency. 
Valid values: true/false​
minBlockTradeAmount​
String​
Specifies the transaction side or direction. Valid values:​
buy​
sell​
orderLimits​
String​
Crypto currency symbol​
> min​
String​
Limit lower value. Ad min and max values should be greater than 
this value.​
> max​
String​
Limit upper value. Ad min and max values should be less than this 
value.​
optimalPrice​
String​
Optimal price for buy/sell ads​
tradableFiatCurrencies​
Array of 
Object​
Tradable fiat currencies based on kyc level of the user​
> currency​
String​
Fiat currency code. Examples: CNY, VND, USD​
 > symbol​
String​
Symbol of fiat currency. Examples: ￥, $​
maxPaymentMethodsAll
owed​
String​
Maximum number of payment methods allowed. Applicable only 
for buy ads​
maxDepositPaymentMet
hodsAllowed​
String​
Maximum number of payment methods allowed. Applicable only 
for sell ads​
maxPaymentDurationAll
owedValues​
String​
Provides possible values for maximum payment duration 
(mayPaymentDuration in create ad API)​
verificationNoteOptions​
Array of 
Object​
Type of verification options that the maker can set to be shown to 
the taker for verification Ads. Only applicable for the CNY region 
for now​
optimalPrices​
Object​
Top buy top sell price​
> 
currentHighestBuyAdPric
e​
String​
Current highest buy ad price​
> 
currentLowestSellAdPric
String​
Current lowest sell ad price​

### Code Examples

```unknown
user is eligible to place block trades. Valid
```

---

---

**📄 Source: PDF Page 32**

e​
2. Order​
2.1 Create Order​
Creates a new ad.​
HTTP Request​
POST /api/v5/p2p/order/create​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​
adId​
String​
Yes​
Ad id for which order would be placed against​
cryptoAmount​
String​
Yes​
Crypto amount. Example: 1.1​
cryptoCurrency​
String​
Yes​
Crypto currency for the ad. Example: "BTC"​
fiatCurrency​
String​
Yes​
Fiat currency for the ad. Example: "USD"​
makerPayment
MethodId​
String​
No​
Maker payment method Id​
paymentMethod​
String​
Yes​
Payment method of the counterparty. When buying crypto, it's 
the payment method of the maker.​
totalFiatAmount​
String​
No​
Total fiat amount for the order. Example: 100.2​
Response Parameters​
Paramete
r​
Type​
Description​
orderId​
String​
Id of the created order​
status​
String​
Order status. Valid values: 2 (new), 3 (cancelled), 4 (completed)​
orderProc
essStatus​
String​
Order process status. Valid values:​
2 (new)​
3 (cancelled)​

---

---

**📄 Source: PDF Page 33**

4 (completed)​
5 (creation in progress)​
6 (creation failed)​
7 (canceling)​
8 (cancellation failed)​
9 (completion in progress)​
10 (completion failed)​
2.2 Get Order
Gets the order information by order id.​
HTTP Request​
GET /api/v5/p2p/order​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Order Id​
Response Parameters​
Parameter​
Type​
Description​
orderId​
String​
Order Id​
side​
String​
Specifies the transaction side or direction. Valid values: buy, sell​
isBlockTradeCategor
y​
Boolean​
Indicates whether the transaction is classified as a block trade​
orderStatus​
String​
Order status. Valid values: new, cancelled, completed​
isFrozen​
Boolean​
Indicates whether the order is frozen​
cryptoCurrency​
String​
Crypto currency symbol​
fiatCurrency​
String​
Fiat currency symbol​
unitPrice​
String​
The unit price of the order​

---

---

**📄 Source: PDF Page 34**

priceMargin​
String​
The price margin ratio for floating type ads. Applicable only for ads 
with price type as floating price​
exchangeRate​
String​
Exchange rate​
cryptoAmount​
String​
The amount of crypto currency traded​
fiatAmount​
String​
The amount of fiat currency traded​
paymentStatus​
String​
The payment status of the order. Valid values: unpaid, paid, 
unreceived, confirmed, rejected​
createdTimestamp​
String​
The timestamp when the order was created​
completionTimesta
mp​
String​
The timestamp when the order was completed​
updatedTimestamp​
String​
The timestamp of the last change made to the order​
completionType​
String​
The type of completion for the order. Example: cancelled_by_buyer​
expiredInSeconds​
String​
The expiration time of the order in seconds​
expiredAfterInSecon
ds​
String​
The expiration duration after completion in seconds​
frozenType​
String​
The type of freeze applied to the order. Valid values: sellerRejectPaid, 
customerService, sellerArbitration, appealFreeze​
disputeStatus​
String​
The dispute status of the order. Valid values: 0 (not appealed), 1 
(maker appealed), 2 (taker appealed), 3 (cancelled), 4 (completed)​
disputeType​
String​
The type of dispute​
disputeSubType​
String​
The subtype of dispute​
disputeResult​
String​
The result of the dispute​
disputeTime​
String​
The time of the dispute​
hasMakerBeenRemin
ded​
Boolean​
Indicates whether the maker has been reminded​
canRaiseDispute​
Boolean​
Indicates whether it is possible to raise dispute​
reviewStatus​
String​
The review status of the order. Valid values: '1' (pending), '2' 
(submitted), '3' (finalised), '4' (expired)​
counterpartyDetail​
Object​
Counterparty details​
> merchantId​
String​
Merchant id​

---

---

**📄 Source: PDF Page 35**

> 
takerPaymentMetho
d​
Object​
Taker collection payment method information​
>> 
paymentMethodId​
String​
Payment method Id​
>> bankCode​
String​
Bank code​
>> bankName
String​
Bank name​
>> bankBranchName​
String​
Bank branch name​
>> accountNo​
String​
Payment method number. This could be bank card number, Alipay 
account number, WeChat Id etc​
>>paymentMethodN
ame​
String​
Payment method name. It could be nick name of the user​
>> 
paymentMethodQrC
odeUrl​
String​
WeChat QR code, Alipay QR code​
>>type​
String​
Payment method type. Examples: BANK, ALIPAY, WXPAY, 
WESTERN_UNION, PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
>> > currency​
String​
Fiat currency symbol. Example: CNY, USD​
>> isDisabled​
Boolean​
Specifies whether the payment method is disabled​
>>decodingUrl​
String​
Payment method QR code decoding URL​
>>paymentDescripti
on​
String​
Payment method description. Example: bank payment, WeChat, 
Alipay​
>> adsLinkedCount​
String​
Number of ads linked to this payment method​
>>isInstantSettlePay
ment​
Boolean​
Indicate whether the payment method instantly settle​
> orders​
String​
Number of buy/sell orders that the user has completed. Example: 10​
> 
estimatedReleaseTi
me​
String​
Estimated crypto release time​
> userId​
String​
User Id​
>nickName​
String​
Nick name of the user​

### Code Examples

```json
user has completed. Example: 10​
```

---

---

**📄 Source: PDF Page 36**

> realName​
String​
Real name of the user​
> type​
String​
User type. Valid values: ​
common​
certified​
diamond​
> completedOrders​
String​
The number of orders completed by the user​
> cancelledOrders​
String​
The number of orders canceled by the user​
> 
completedSellOrders​
String​
The number of sell orders completed by the user​
>completionRate​
String​
The order completion rate of the user​
>kycLevel​
String​
The identity verification level of the user​
>acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do not accept 
order), 1 (accept order)​
>avgPaymentTimeIn
Seconds​
String​
Average payment time in seconds​
>avgCompletionTim
eInSeconds​
String​
Average completion time in seconds​
>createdTimestamp​
String​
User joining timestamp in milliseconds​
>hasAlreadyTraded​
Boolean​
Specifies whether the user has traded in the past with the requester. 
Valid values: true, false​
2.3 Get Orders by Filters​
Get the order list filtered by parameters. Users can get the order list for the last 6 months.​
HTTP Request​
GET /api/v5/p2p/order/list​
Request Parameters​
Parameter​
Type​
Require
d​
Description​

### Code Examples

```unknown
user has traded in the past with the requester.
```

```json
user. Valid values: 0 (do not accept
```

---

---

**📄 Source: PDF Page 37**

side​
String​
No​
Specifies the transaction side or direction. Use buy to indicate a 
buy transaction, sell for a sell transaction, or all to include both buy 
and sell transactions. Default: all​
pageIndex​
String​
Yes​
Page index starting from 1. Default: 1​
pageSize​
String​
Yes​
Number of orders to fetch. Default: 20​
cryptoCurre
ncies​
String​
No​
Specifies crypto currencies. Valid values are comma-separated 
crypto currency symbols. Example: BTC, ETH​
fiatCurrenci
es​
String​
No​
Specifies fiat currencies. Valid values are comma-separated fiat 
currency symbols. Example: CNY,USD​
start​
String​
No​
Search start timestamp. Unix timestamp format in milliseconds.​
end​
String​
No​
Search end timestamp. Unix timestamp format in milliseconds.​
completion
Status​
String​
No​
Specifies completion status category. Valid values:​
all - all types of order are needed ​
pending - orders which aren't completed/cancelled​
completed - orders which are completed/cancelled​
Default: all​
searchKeyw
ord​
String​
No​
Search orders by either Order Id or User nickname​
Response Parameters​
Parameter​
Type​
Description​
adId​
String​
Id of the Ad against which order was placed​
orderId​
String​
Order Id​
side​
String​
Specifies the transaction side or direction. Valid values: buy, 
sell​
isBlockTradeCateg
ory​
Boolea
n​
Indicates whether the transaction is classified as a block trade​
orderStatus​
String​
Order status. Valid values: new, cancelled, completed​
isFrozen​
Boolea
n​
Indicates whether the order is frozen​

### Code Examples

```unknown
include both buy
```

---

---

**📄 Source: PDF Page 38**

cryptoCurrency​
String​
Crypto currency symbol​
fiatCurrency​
String​
Fiat currency symbol​
unitPrice​
String​
The unit price of the order​
priceMargin​
String​
The price margin ratio for floating type ads. Applicable only 
for ads with price type as floating price​
exchangeRate​
String​
Exchange rate​
cryptoAmount​
String​
The amount of crypto currency traded​
fiatAmount​
String​
The amount of fiat currency traded​
paymentStatus​
String​
The payment status of the order. Valid values: unpaid, paid, 
unreceived, confirmed, rejected​
createdTimestamp​
String​
The timestamp when the order was created​
completedTimesta
mp​
String​
The timestamp when the order was completed​
updatedTimestam
p​
String​
The timestamp of the last change made to the order​
completionType​
String​
The type of completion for the order. Example: 
cancelled_by_buyer​
expiredInSeconds​
String​
The expiration time of the order in seconds​
expiredAfterInSeco
nds​
String​
The expiration duration after completion in seconds​
frozenType​
String​
The type of freeze applied to the order. Valid values: 
sellerRejectPaid, customerService, sellerArbitration, 
appealFreeze​
disputeStatus​
String​
The dispute status of the order. Valid values: 0 (not appealed), 
1 (maker appealed), 2 (taker appealed), 3 (cancelled), 4 
(completed)​
disputeType​
String​
The type of dispute​
disputeSubType​
String​
The subtype of dispute​
disputeResult​
String​
The result of the dispute​
disputeTime​
String​
The time of the dispute​

---

---

**📄 Source: PDF Page 39**

hasMakerBeenRe
minded​
Boolea
n​
Indicates whether the maker has been reminded​
canRaiseDispute​
Boolea
n​
Indicates whether it is possible to raise dispute​
reviewStatus​
String​
The review status of the order. Valid values: '1' (pending), '2' 
(submitted), '3' (finalised), '4' (expired)​
counterpartyDetail​
Object​
Counterparty details​
>merchantId​
String​
Merchant id​
>takerPaymentMet
hod​
Object​
Taker collection payment method information​
>>paymentMethod
Id​
String​
Payment method Id​
>>bankCode​
String​
Bank code​
>>bankName​
String​
Bank name​
>>bankBranchNa
me​
String​
Bank branch name​
>>paymentMethod
Number​
String​
Payment method number. This could be bank card number, 
Alipay account number, WeChat Id etc​
>>paymentMethod
Name​
String​
Payment method name. It could be nick name of the user​
>>paymentMethod
QrCodeUrl​
String​
WeChat QR code, Alipay QR code​
>>type​
String​
Payment method type. Examples: BANK, ALIPAY, WXPAY, 
WESTERN_UNION, PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
>>>currency​
String​
Fiat currency symbol. Example: CNY, USD​
>>isDisabled​
Boolea
n​
Specifies whether the payment method is disabled​
>>decodingUrl​
String​
Payment method QR code decoding URL​
>>paymentDescrip
tion​
String​
Payment method description. Example: bank payment, 
WeChat, Alipay​
>>adsLinkedCount​
String​
Number of ads linked to this payment method​

---

---

**📄 Source: PDF Page 40**

>>isInstantSettleP
ayment​
Boolea
n​
Indicate whether the payment method instantly settle​
>orders​
String​
Number of buy/sell orders that the user has completed. 
Example: 10​
>estimatedRelease
Time​
String​
Estimated crypto release time​
>id​
String​
User Id​
>nickName​
String​
Nick name of the user​
>realName​
String​
Real name of the user​
>targetGroup​
String​
User target group for the ad. Valid values: ​
common​
certified​
diamond​
all​
>completedOrders​
String​
The number of orders completed by the user​
>cancelledOrders​
String​
The number of orders canceled by the user​
>completedSellOr
ders​
String​
The number of sell orders completed by the user​
>completionRate​
String​
The order completion rate of the user​
>kycLevel​
String​
The identity verification level of the user​
>acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do not 
accept order), 1 (accept order)​
>avgPaymentTime
InSeconds​
String​
Average payment time in seconds​
>avgCompletionTi
meInSeconds​
String​
Average completion time in seconds​
>createdTimestam
p​
String​
User joining timestamp in milliseconds​
>hasAlreadyTrade
d​
Boolea
n​
Specifies whether the user has traded in the past with the 
requester. Valid values: true, false​

### Code Examples

```unknown
user has traded in the past with the
```

```unknown
user has completed.
```

```json
user. Valid values: 0 (do not
```

---

---

**📄 Source: PDF Page 41**

2.4 Get Counterparty User Details​
Obtain counterparty user information for the order.​
HTTP Request​
GET /api/v5/p2p/order/counterparty-user-info​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Order id​
Response Parameters​
Parameter​
Type​
Description​
merchantId​
String​
Merchant id​
takerPaymentMeth
od​
Object​
Taker collection payment method information​
>paymentMethodI
d​
String​
Payment method Id​
>bankCode​
String​
Bank code​
>bankName​
String​
Bank name​
>bankBranchName​
String​
Bank branch name​
>paymentMethodN
umber​
String​
Payment method number. This could be bank card number, Alipay 
account number, WeChat Id etc​
>paymentMethodN
ame​
String​
Payment method name. It could be nick name of the user​
>paymentMethodQ
rCodeUrl​
String​
WeChat QR code, Alipay QR code​
>type​
String​
Payment method type. Examples: BANK, ALIPAY, WXPAY, 
WESTERN_UNION, PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
>currency​
String​
Fiat currency symbol. Example: CNY, USD​

### Code Examples

```unknown
user information for the order.​
```

---

---

**📄 Source: PDF Page 42**

>isDisabled​
String​
Specifies whether the payment method is disabled​
>decodingUrl​
String​
Payment method QR code decoding URL​
>paymentDescripti
on​
String​
Payment method description. Example: bank payment, WeChat, Alipay​
>adsLinkedCount​
String​
Number of ads linked to this payment method​
>isInstantSettlePay
ment​
String​
Indicate whether the payment method instantly settle​
orders​
String​
Number of buy/sell orders that the user has completed. Example: 10​
estimatedReleaseT
ime​
String​
Estimated crypto release time​
userId ​
String​
User Id​
nickName​
String​
Nick name of the user​
realName​
String​
Real name of the user​
type
String​
User type. Valid values: ​
common​
certified​
diamond​
completedOrders​
String​
The number of orders completed by the user​
cancelledOrders​
String​
The number of orders canceled by the user​
completedSellOrde
rs​
String​
The number of sell orders completed by the user​
completionRate​
String​
The order completion rate of the user​
kycLevel​
String​
The identity verification level of the user​
acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do not accept 
order), 1 (accept order)​
avgPaymentTimeIn
Seconds​
String​
Average payment time in seconds​
avgCompletionTim
eInSeconds​
String​
Average completion time in seconds​
createdTimestamp​
String​
User joining timestamp in milliseconds​

### Code Examples

```json
user has completed. Example: 10​
```

```json
user. Valid values: 0 (do not accept
```

---

---

**📄 Source: PDF Page 43**

hasAlreadyTraded​
Boolean​
Specifies whether the user has traded in the past with the requester. 
Valid values: true, false​
2.5 Get Batch Counterparty Details for Orders​
Obtain multiple counterparty user information for the orders.​
HTTP Request​
POST /api/v5/p2p/order/counterparty-user-list​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
orderIds​
String​
Yes​
Order Ids
Response Parameters​
Parameter​
Type​
Description​
orderId​
String​
Order Id​
realName​
Object​
Actual name of the counterparty​
2.6 Get Trade Summary with User​
Get a list of order cancellation reasons.​
HTTP Request​
GET /api/v5/p2p/order/trade-info​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
userId​
String​
Yes​
Id of the user for which trade info is needed​
Response Parameters​

### Code Examples

```unknown
user has traded in the past with the requester.
```

```unknown
user information for the orders.​
```

```unknown
user for which trade info is needed​
```

---

---

**📄 Source: PDF Page 44**

Paramete
r​
Type​
Description​
tradeCoun
t​
String​
Number of trades​
tradeAmo
unt​
String​
Total amount traded​
side​
String​
Specifies the transaction side or direction. ​
2.7 Get Pending Order Details​
Obtain pending order details for an ad.​
HTTP Request​
GET /api/v5/p2p/order/pending-order​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
adId​
String​
Yes​
Ad id​
Response Parameters​
Parameter​
Type​
Description​
orderId​
String​
Order Id​
side​
String​
Specifies the transaction side or direction. Valid values: buy, sell​
isBlockTradeCategory
Boolean​
Indicates whether the transaction is classified as a block trade​
orderStatus​
String​
Order status. Valid values: new, cancelled, completed​
isFrozen​
Boolean​
Indicates whether the order is frozen​
cryptoCurrency​
String​
Crypto currency symbol​
fiatCurrency​
String​
Fiat currency symbol​
unitPrice​
String​
The unit price of the order​
priceMargin​
String​

---

---

**📄 Source: PDF Page 45**

The price margin ratio for floating type ads. Applicable only for ads 
with price type as floating price​
exchangeRate​
String​
Exchange rate​
cryptoAmount​
String​
The amount of crypto currency traded​
fiatAmount​
String​
The amount of fiat currency traded​
paymentStatus​
String​
The payment status of the order. Valid values: unpaid, paid, 
unreceived, confirmed, rejected​
createdTimestamp​
String​
The timestamp when the order was created​
completionTimestamp​
String​
The timestamp when the order was completed​
updatedTimestamp​
String​
The timestamp of the last change made to the order​
completionType​
String​
The type of completion for the order. Example: cancelled_by_buyer​
expiredInSeconds​
String​
The expiration time of the order in seconds​
expiredAfterInSeconds​
String​
The expiration duration after completion in seconds​
frozenType​
String​
The type of freeze applied to the order. Valid values: 
sellerRejectPaid, customerService, sellerArbitration, appealFreeze​
disputeStatus​
String​
The dispute status of the order. Valid values: 0 (not appealed), 1 
(maker appealed), 2 (taker appealed), 3 (cancelled), 4 (completed)​
disputeType​
String​
The type of dispute​
disputeSubType​
String​
The subtype of dispute​
disputeResult​
String​
The result of the dispute​
disputeTime​
String​
The time of the dispute​
hasMakerBeenRemind
ed​
Boolean​
Indicates whether the maker has been reminded​
canRaiseDispute​
Boolean​
Indicates whether it is possible to raise dispute​
reviewStatus​
String​
The review status of the order. Valid values: '1' (pending), '2' 
(submitted), '3' (finalised), '4' (expired)​
counterpartyDetail​
Object​
Counterparty details​
>merchantId​
String​
Merchant id​
>takerPaymentMethod​
Object​
Taker collection payment method information​

---

---

**📄 Source: PDF Page 46**

>>paymentMethodId​
String​
Payment method Id​
>>bankCode​
String​
Bank code​
>>bankName​
String​
Bank name​
>>bankBranchName​
String​
Bank branch name​
>>paymentMethodNu
mber​
String​
Payment method number. This could be bank card number, Alipay 
account number, WeChat Id etc​
>>paymentMethodNa
me​
String​
Payment method name. It could be nick name of the user​
>>paymentMethodQrC
odeUrl​
String​
WeChat QR code, Alipay QR code​
>>type​
String​
Payment method type. Examples: BANK, ALIPAY, WXPAY, 
WESTERN_UNION, PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
>>>currency​
String​
Fiat currency symbol. Example: CNY, USD​
>>isDisabled​
Boolean​
Specifies whether the payment method is disabled​
>>decodingUrl​
String​
Payment method QR code decoding URL​
>>paymentDescription​
String​
Payment method description. Example: bank payment, WeChat, 
Alipay​
>>adsLinkedCount​
String​
Number of ads linked to this payment method​
>>isInstantSettlePaym
ent​
String​
Indicate whether the payment method instantly settle​
>orders​
String​
Number of buy/sell orders that the user has completed. Example: 10​
>estimatedReleaseTim
e​
String​
Estimated crypto release time​
>userId​
String​
User Id​
>nickName​
String​
Nick name of the user​
>realName​
String​
Real name of the user​
>targetGroup​
String​
User target group for the ad. Valid values: ​
common​
certified​
diamond​

### Code Examples

```json
user has completed. Example: 10​
```

---

---

**📄 Source: PDF Page 47**

all​
>completedOrders​
String​
The number of orders completed by the user​
>cancelledOrders​
String​
The number of orders canceled by the user​
>completedSellOrders​
String​
The number of sell orders completed by the user​
>completionRate​
String​
The order completion rate of the user​
>kycLevel​
String​
The identity verification level of the user​
>acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do not accept 
order), 1 (accept order)​
>avgPaymentTimeInS
econds​
String​
Average payment time in seconds​
>avgCompletionTimeI
nSeconds​
String​
Average completion time in seconds​
>createdTimestamp​
String​
User joining timestamp in milliseconds​
>hasAlreadyTraded​
Boolean​
Specifies whether the user has traded in the past with the 
requester. Valid values: true, false​
2.8 Mark Order as Paid​
Lets buyer mark the order as paid.​
HTTP Request​
POST /api/v5/p2p/order/mark-as-paid
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​
orderId​
String​
Yes​
Id of the order for which payment is made​
paymentProofFil
eUrls​
String​
No​
Collections of payment proof file url​
makerPaymentM
ethodId​
String​
No​
Maker payment method id​
rrnCode​
String​
No​
Retrieval Reference Number​

### Code Examples

```unknown
user has traded in the past with the
```

```json
user. Valid values: 0 (do not accept
```

---

---

**📄 Source: PDF Page 48**

Response Parameters​
Paramete
r​
Type​
Description​
orderId​
String​
Id of the order for which payment is made​
2.9 Cancel Order​
Cancels the order. Buyers cancel pending, unpaid, paid, or rejected orders, and sellers cancel 
pending orders​
HTTP Request​
POST /api/v5/p2p/order/cancel​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Id of the Order to be canceled​
verificati
onType​
String​
Yes​
Valid values:​
1, 2​
Use 2 currently​
amount​
String​
No​
Amount for which the order was placed. Example: 1.2​
Response Parameters​
Paramete
r​
Type​
Description​
orderId​
String​
Id of the order which got cancelled​
2.10 Mark Order as Unpaid​
Lets seller mark the order as unpaid.​
HTTP Request​
POST /api/v5/p2p/order/mark-as-unpaid​

---

---

**📄 Source: PDF Page 49**

Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Id of the order for which payment should be marked as unpaid​
Response Parameters​
Paramete
r​
Type​
Description​
orderId​
String​
Id of the order for which payment is marked as unpaid
2.11 Release Crypto​
Seller can release the crypto upon confirming the payment.​
HTTP Request​
POST /api/v5/p2p/order/release-crypto​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​
orderId​
String​
Yes​
Id of the order for which crypto should be released​
paymentProofFil
eUrls​
String​
No​
Collections of payment proof file url​
verificationType​
String​
Yes​
Valid values:​
1, 2​
Use 2 currently​
amount​
String​
No​
Amount received from the buyer. Example: 1.2​
Response Parameters​
Paramete
r​
Type​
Description​

---

---

**📄 Source: PDF Page 50**

orderId​
String​
Id of the order for which crypto is released​
2.12 Get Cancellation Reasons​
Get a list of order cancellation reasons.​
HTTP Request​
GET /api/v5/p2p/order/cancel-reason-list​
Request Parameters​
Parame
ter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Order Id​
Request Parameters​
Paramete
r​
Type​
Description​
reasonId​
String​
Reason Id​
reason​
String​
Cancellation reason​
subReaso
ns​
Array of 
Object​
Sub reasons​
>reasonId​
String​
Sub-reason Id​
>reason​
String​
Cancellation sub-reason​
2.13 Get Unreleased Orders​
Get order ids that haven't been processed for a long time.​
HTTP Request​
GET /api/v5/p2p/order/unreleased-orders​
Response Parameters​
Paramete
r​
Type​
Description​

---

---

**📄 Source: PDF Page 51**

orderIds​
Array of 
String​
Unreleased order Ids​
waitingTi
meInMinu
tes​
String​
Waiting time in minutes​
3. Payment Method​
3.1 Add Payment Method​
Adds a new payment method.​
HTTP Request​
GET /api/v5/p2p/payment-method/add​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
currency​
String​
Yes​
Fiat currency symbol. Examples: CNY, VND​
type
String​
Yes​
Type of payment method. Examples: BANK, ALIPAY, WXPAY, 
WESTERN_UNION, PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
isEnabled​
Boolean​
Yes​
Specifies whether payment method should be enabled. Valid 
values: true, false​
application
Type​
String​
Yes​
Type of application. Valid values: -1: (Disabled) 0 (Enabled), 1 
(Deposit payment method, used for receiving payment), 2 
(Withdrawal Payment method, used for paying)​
details​
Object​
Yes​
Key-value pairs of fields required for adding payment method 
where key is field name and value is field value. Example: 
{"accountNo": "1234"}​
Response Parameters​
Paramete
r​
Type​
Description​
payment
MethodId​
String​
Id of the added Payment method​

### Code Examples

```unknown
used for receiving payment), 2
```

```unknown
required for adding payment method
```

```unknown
used for paying)​
```

---

---

**📄 Source: PDF Page 52**

3.2 Get Payment Method​
Get payment method info.​
HTTP Request​
GET /api/v5/p2p/payment-method
Request Parameters​
Parameter​
Type​
Require
d​
Description​
paymentM
ethodId​
String​
Yes​
Payment method id​
Response Parameters​
Paramete
r​
Type​
Description​
payment
MethodId​
String​
Payment method Id​
bankCode​
String​
Bank code​
bankNam
e​
String​
Bank name​
bankBran
chName​
String​
Bank branch name​
payment
MethodN
umber​
String​
Payment method number. This could be bank card number, Alipay account 
number, WeChat Id etc​
payment
MethodN
ame​
String​
Payment method name. It could be nick name of the user​
payment
MethodQr
CodeUrl​
String​
WeChat QR code, Alipay QR code​
type
String​

---

---

**📄 Source: PDF Page 53**

Payment method type. Examples: BANK, ALIPAY, WXPAY, WESTERN_UNION, 
PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
currency​
String​
Fiat currency symbol. Example: CNY, USD​
isDisable
d​
Boolean​
Specifies whether the payment method is disabled​
decoding
Url​
String​
Payment method QR code decoding URL​
payment
Descriptio
n​
String​
Payment method description. Example: bank payment, WeChat, Alipay​
adsLinked
Count​
String​
Number of ads linked to this payment method​
isInstantS
ettlePaym
ent​
Boolean​
Indicate whether the payment method instantly settle​
3.3 Get Payment Methods​
Get all payment methods.​
HTTP Request​
GET /api/v5/p2p/payment-method/list​
Response Parameters​
Paramete
r​
Type​
Description​
payment
MethodId​
String​
Payment method Id​
bankCode​
String​
Bank code​
bankNam
e​
String​
Bank name​
bankBran
chName​
String​
Bank branch name​
payment
MethodN
String​
Payment method number. This could be bank card number, Alipay account 
number, WeChat Id etc​

---

---

**📄 Source: PDF Page 54**

umber​
payment
MethodN
ame​
String​
Payment method name. It could be nick name of the user​
payment
MethodQr
CodeUrl​
String​
WeChat QR code, Alipay QR code​
type
String​
Payment method type. Examples: BANK, ALIPAY, WXPAY, WESTERN_UNION, 
PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
currency​
String​
Fiat currency symbol. Example: CNY, USD​
isDisable
d​
Boolean​
Specifies whether the payment method is disabled​
decoding
Url​
String​
Payment method QR code decoding URL​
payment
Descriptio
n​
String​
Payment method description. Example: bank payment, WeChat, Alipay​
adsLinked
Count​
String​
Number of ads linked to this payment method​
isInstantS
ettlePaym
ent​
Boolean​
Indicate whether the payment method instantly settle​
3.4 Update Payment Method​
Update the payment method.
HTTP Request​
POST /api/v5/p2p/payment-method/update​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
paymentM
ethodId​
String​
Yes​
Id of the Payment Method which needs to be updated​

---

---

**📄 Source: PDF Page 55**

currency​
String​
Yes​
Fiat currency symbol. Examples: CNY, VND​
type
String​
Yes​
Type of payment method. Examples: BANK, ALIPAY, WXPAY, 
WESTERN_UNION, PAY_PAL, SWIFT, PAY_NOW, PAYTM, QIWI​
isEnabled​
Boolean​
Yes​
Specifies whether payment method should be enabled. Valid 
values: true, false​
application
Type​
String​
Yes​
Type of application. Valid values: -1: (Disabled) 0 (Enabled), 1 
(Deposit payment method, used for receiving payment), 2 
(Withdrawal Payment method, used for paying)​
details​
Object​
Yes​
Key-value pairs of fields required for adding payment method 
where key is field name and value is field value. Example: 
{"accountNo": "1234"}​
Response Parameters​
Paramete
r​
Type​
Description​
payment
MethodId​
String​
Id of the updated Payment method​
3.5 Delete Payment Method​
Delete the payment method.​
HTTP Request​
GET /api/v5/p2p/payment-method/delete​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
paymentM
ethodId​
String​
Yes​
Id of the Payment Method which needs to be deleted​
Response Parameters​
Paramete
r​
Type​
Description​

### Code Examples

```unknown
used for receiving payment), 2
```

```unknown
required for adding payment method
```

```unknown
used for paying)​
```

---

---

**📄 Source: PDF Page 56**

payment
MethodId​
String​
Id of the Payment Method which got deleted​
3.6 Update Payment Method Status​
Delete the payment method.​
HTTP Request​
GET /api/v5/p2p/payment-method/update-status​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
paymentM
ethodId​
String​
Yes​
Payment Method Id for which status needs to be updated​
disable​
Boolean​
Yes​
Specifies whether to disable the payment method​
Response Parameters​
Paramete
r​
Type​
Description​
payment
MethodId​
String​
Id of the Payment Method for which status got updated​
3.7 Get Supported Payment Methods​
Get all payment methods which are supported by the currencies specified.​
HTTP Request​
GET /api/v5/p2p/payment-method/supported-list​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
currencies​
String​
Yes​
Fiat currencies for which supported payment methods are needed. 
Valid values are comma-separated fiat currency symbols. Example:

---

---

**📄 Source: PDF Page 57**

CNY,USD​
Response Parameters​
Parameter​
Type​
Description​
paymentMetho
d​
String​
Payment method​
icon​
String​
Icon for the payment method​
applicationTyp
e​
String​
Type of application. Valid values: -1: (Disabled) 0 (Enabled), 1 (Deposit 
payment method, used for receiving payment), 2 (Withdrawal Payment 
method, used for paying)​
currency​
String​
Fiat currency symbol​
4. P2P Ticker​
4.1 Get Swap Price​
Get Swap Price.​
HTTP Request​
GET /api/v5/p2p/p2p-ticker/swap​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
cryptoCurr
ency​
String​
Yes​
The crypto currency symbol. Example: BTC​
fiatCurrenc
y​
String​
Yes​
The fiat currency symbol. Example: USD​
usdtAmou
nt​
String​
Yes​
Amount of USDT​
Response Parameters​
Type​
Description​

### Code Examples

```unknown
used for receiving payment), 2 (Withdrawal Payment
```

```unknown
used for paying)​
```

---

---

**📄 Source: PDF Page 58**

Paramete
r​
price​
String​
Price​
swapFiatI
d​
String​
Swap fiat Id​
swapAmo
unt​
String​
Exchange amount​
swapFiat
Scale​
String​
Conversion quantity accuracy​
fiatSymb
ol​
String​
Fiat currency symbol. Examples: ￥,$​
4.2 Get All Crypto prices​
Get all crypto prices for a fiat currency.​
HTTP Request​
GET /api/v5/p2p/p2p-ticker/all​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
fiatCurrenc
y​
String​
Yes​
The fiat currency symbol. Example: USD​
Response Parameters​
Paramete
r​
Type​
Description​
prices​
String​
Mapping of Crypto currency symbol to price. Example: BTC -> 0.01​
4.3 Get Platform ticker price​
Get the price for the currency pair.​
HTTP Request​

---

---

**📄 Source: PDF Page 59**

GET /api/v5/p2p/p2p-ticker/platform-ticker​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
price​
String​
Yes​
Price​
Response Parameters​
Paramete
r​
Type​
Description​
price​
String​
Price for the currency pair​
4.4 Get Estimated price​
Get estimated trading price for the currency pair.​
HTTP Request​
GET /api/v5/p2p/p2p-ticker/estimated-price​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
cryptoCurr
ency​
String​
Yes​
The crypto currency symbol. Example: BTC​
fiatCurrenc
y​
String​
Yes​
The fiat currency symbol. Example: USD​
side​
String​
No​
Specifies the transaction side or direction. Use buy to indicate a buy 
transaction, sell for a sell ​
transaction.​
depositNa
me​
String​
No​
Deposit name. Example: 'OKEX P2P'​
paymentM
ethod​
String​
No​
Payment method. Example: bank​

---

---

**📄 Source: PDF Page 60**

Response Parameters​
Paramete
r​
Type​
Description​
price​
String​
Price for the currency pair​
5. User​
5.1 Get Basic Information​
Gets the basic information for the user. ​
HTTP Request​
GET /api/v5/p2p/user/basic-info​
Response Parameters​
Parameter​
Type​
Description​
userId​
String​
User Id​
nickName​
String​
Nick name of the user​
realName​
String​
Real name of the user​
phoneNumber​
String​
Phone number of the user​
email​
String​
Email of the user​
type
String​
User type. Valid values: ​
common​
certified​
diamond​
completedOrders​
String​
The number of orders completed by the user​
completedSellOrders​
String​
The number of sell orders completed by the user​
cancelledOrders​
String​
The number of orders canceled by the user​
completionRate​
String​
The order completion rate of the user​
kycLevel​
String​
The identity verification level of the user. Valid values: 1, 2, 3​

### Code Examples

```unknown
user/basic-info​
```

```json
user. Valid values: 1, 2, 3​
```

---

---

**📄 Source: PDF Page 61**

acceptStatus​
String​
Order acceptance status of the user. Valid values: 0 (do not accept 
order), 1 (accept order)​
avgPaymentTimeInSe
conds​
String​
Average payment time in seconds​
avgCompletionTimeI
nSeconds​
String​
Average completion time in seconds​
createdTimestamp​
String​
User joining timestamp in milliseconds​
5.2 Get Id for UID​
Get P2P user Id by UID (visible on Web/Mobile).​
HTTP Request​
GET /api/v5/p2p/user/id​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
uid​
String​
Yes​
UID of the user​
Response Parameters​
Paramete
r​
Type​
Description​
userId​
String​
User Id of the user​
5.3 Get Balance​
Get balance for the user.​
HTTP Request​
GET /api/v5/p2p/user/balance​
Request Parameters​
Parameter​
Type​
Require
d​
Description​

### Code Examples

```unknown
user Id by UID (visible on Web/Mobile).​
```

```json
user. Valid values: 0 (do not accept
```

---

---

**📄 Source: PDF Page 62**

currencySy
mbol​
String​
Yes​
Currency symbol. Example: BTC​
Response Parameters​
Parameter​
Type​
Description​
availableAmount​
String​
The available crypto quantity currently available for buying and selling​
onHoldAmount​
String​
The quantity that has been frozen but the order has not been 
completed till now​
sellOrTransferLimit​
String​
Sell or transfer limit​
currencySymbol​
String​
Currency symbol. Example: BTC​
isSecurityLimitAppl
icable​
Boolean​
Specifies whether the ad is T+1 ad​
5.4 Get Blacklist Users​
Get details of blacklisted users.​
HTTP Request​
GET /api/v5/p2p/user/blacklist-users​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
currencySy
mbol​
String​
Yes​
Currency symbol. Example: BTC​
Response Parameters​
Parameter​
Type​
Description​
userName​
String​
User name​
createdTimestamp​
String​
Timestamp of the blacklisted action. Unix timestamp format in 
milliseconds

### Code Examples

```unknown
user/blacklist-users​
```

---

---

**📄 Source: PDF Page 63**

buyerAvgPaidTime​
String​
The buyer average payment time in minutes​
sellerAvgComplete
dTime​
String​
The seller's average release time in minutes​
userType​
String​
User type. Valid values: common,certified,diamond​
completionRate​
String​
Completion rate​
orders​
String​
Number of total order. Includes completed and cancelled orders​
userId​
String​
User Id​
5.5 Add Blacklist User​
Add user to the blacklist.​
HTTP Request​
POST /api/v5/p2p/user/add-user-to-blacklist​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
userId​
String​
Yes​
Id of the user who needs to be blacklisted​
reasons​
String​
No​
Reasons for blacklisting. Comma separated reasons can be provided​
otherReas
on​
String​
No​
Any other reason for blocking​
orderId​
String​
No​
Order Id​
Response Parameters​
Parameter​
Type​
Description​
userId​
String​
Id of the user who got blacklisted​
5.6 Remove User from Blacklist ​
Add user to the blacklist.​
HTTP Request​

### Code Examples

```unknown
user to the blacklist.​
```

```unknown
user/add-user-to-blacklist​
```

```unknown
user who needs to be blacklisted​
```

```unknown
user who got blacklisted​
```

---

---

**📄 Source: PDF Page 64**

POST /api/v5/p2p/user/remove-user-from-blacklist​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
userId​
String​
Yes​
Id of the user who needs to be removed from the blacklist​
Response Parameters​
Parameter​
Type​
Description​
userId​
String​
Id of the user who got removed from the blacklist​
5.7 Get User statistics​
Get current user badge related information.​
HTTP Request​
GET /api/v5/p2p/user/statistics​
Response Parameters​
Parameter​
Type​
Description​
newOrders​
String​
Number of Orders in progress​
newAds​
String​
Number of ads in progress​
appealOrders​
String​
Number of orders in appeal​
completedAppealO
rders​
String​
Number of completed orders with appeal​
cancelledAppealOr
ders​
String​
Number of cancelled orders with appeal​
waitPaidOrders​
String​
Number of orders pending payment​
waitReleaseOrder​
String​
Number of to-be-released orders​
cancelledOrders​
String​
Number of orders canceled by the user​
completedOrders​
String​
Number of orders the user has completed​

### Code Examples

```sql
user who needs to be removed from the blacklist​
```

```sql
user who got removed from the blacklist​
```

```unknown
user/remove-user-from-blacklist​
```

```unknown
user badge related information.​
```

```unknown
user/statistics​
```

```unknown
user has completed​
```

---

---

**📄 Source: PDF Page 65**

pendingActions​
String​
Number of user's pending actions​
5.8 Update Online Status​
Updates user online status. If the user chooses to be offline, no ad can be placed against the ads 
created by the user.​
HTTP Request​
POST /api/v5/p2p/user/update-online-status​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
status​
String​
Yes​
User online status. Valid values: hidden (makes user offline), show 
(makes user online)​
Response Parameters​
Parameter​
Type​
Description​
status​
String​
Updated online status​
6. Merchant​
6.1 Get Basic Information​
Gets the basic information of the merchant. ​
HTTP Request​
GET /api/v5/p2p/merchant/basic-info​
Response Parameters​
Parameter​
Type​
Description​
nickname​
String​
Nick name of the user​
avatarImage​
String​
User image URL​
description​
String​
Description of the merchant​

### Code Examples

```unknown
user's pending actions​
```

```unknown
user online status. If the user chooses to be offline, no ad can be placed against the ads
```

```unknown
user/update-online-status​
```

```unknown
user offline), show
```

---

---

**📄 Source: PDF Page 66**

status​
String​
Status of the merchant. Valid values: 0 (under review), 1 (passed 
review), -1 (rejected)​
remark​
String​
Remark​
6.2 Get Merchant info by share code​
Get shared information by sharing code. ​
HTTP Request​
GET /api/v5/p2p/merchant/share-info​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
shareCode​
String​
Yes​
Share Code​
Response Parameters​
Parameter​
Type​
Description​
realName​
String​
Real name of the user​
userId​
String​
Id of the user​
completedOrd
ers​
String​
Number of orders completed by the user​
completionRat
e​
String​
Completion rate​
isSelf​
Boolean​
Specifies whether the user is the requester​
6.3 Get sharable basic info​
Gets the basic information of the merchant along with the QR code which can be shared. ​
HTTP Request​
GET /api/v5/p2p/merchant/share-profile​
Response Parameters​

### Code Examples

```unknown
user is the requester​
```

---

---

**📄 Source: PDF Page 67**

Parameter​
Type​
Description​
merchantId​
String​
Id of the Merchant​
avatarImage​
String​
User image URL​
totalOrders​
String​
Total orders​
tradedUsers​
String​
Number of people merchant traded with​
currencyPairs
Array of 
Object​
Collection of currencies the merchant traded in.​
> cryptoCurrency​
String​
The crypto currency symbol. Example: BTC​
> fiatCurrency​
String​
The fiat currency symbol. Example: USD​
qrCode​
String​
Share link​
password​
String​
Share password​
6.4 Get Profile Information​
Get merchant's profile (from the merchant himself/herself, or from others). ​
HTTP Request​
GET /api/v5/p2p/merchant/profile​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
userId​
String​
No​
Id of the user for which information in required​
Response Parameters​
Parameter​
Type​
Description​
merchantId​
String​
Id of the Merchant​
avatarImage​
String​
User image URL​
auditStatus​
String​
Audit status. Valid values: -1 (audit failed), 0 (audit in progress), 1 
(audit passed), 2 (initialization completed, after N hours of audit 
passed, the status changes to this status​

### Code Examples

```bash
user for which information in required​
```

---

---

**📄 Source: PDF Page 68**

completedBuyOrders​
String​
Total completed buy orders​
tradedUsers​
String​
Number of people merchant traded with​
merchantInfo30DayOr
derInfo​
Array of 
Object​
30 day order info​
> 
completedOrders30Da
y​
String​
30 day completed orders count​
> 
servedUsersComplete
dOrders30Day​
String​
The number of users served for completed orders within 30 days​
> 
completionRate30Day​
String​
30 day completion rate​
> 
completionRateBuyOr
ders30Day​
String​
30 day completion rate for buy orders​
> 
completionRateSellOr
ders30Day​
String​
30 day completion rate for sell orders​
positiveReviews​
String​
Number of positive reviews​
negativeReviews​
String​
Number of negative reviews​
positiveReviewPercent
age​
String​
Positive review percentage​
totalReviews​
String​
Number of reviews given for the user​
commonOrderTotal​
String​
The total transaction amount of the current site within half a year 
(usd)​
blacklistUserCount​
String​
Number of times the user has been blocked​
followerCount​
String​
Followers count
isDisabled​
Boolean​
Specifies whether the account is frozen​
countryId​
String​
KYC country​
merchantRegisteredTi
mestamp​
String​
Merchant registration timestamp. Unix timestamp format in 
milliseconds

### Code Examples

```unknown
users served for completed orders within 30 days​
```

```unknown
user has been blocked​
```

---

---

**📄 Source: PDF Page 69**

countryName​
String​
Country name​
countryIcon​
String​
Country flag​
isKycVerified​
Boolean​
Specifies whether the merchant is KYC verified​
isPhoneVerified​
Boolean​
Specifies whether the user has completed phone verification​
isEmailVerified​
Boolean​
Specifies whether the user has completed email verification ​
blacklistStatus​
String​
Blacklist status of the user. Valid values: NO_BLACK (No blacklist 
relationship), BLACK_OTHER (Current user blacklisted the other 
side), BLACKED (The other side blacklisted current user), 
BLACK_EACH_OTHER (Current user and other use blacklisted each 
other)​
isFollowingUser​
Boolean​
Specifies whether the requester follows the user​
isSelf​
Boolean​
Specifies whether the requester is the user itself​
depositAmount​
String​
Merchant's deposit amount​
depositCurrency​
String​
Merchant's deposit currency​
6.5 Get Merchant Ads​
Get merchant's add list (not for merchant himself/herself). ​
HTTP Request​
GET /api/v5/p2p/merchant/ads​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
userId​
String​
Yes​
Id of the user for which ads are required​
Response Parameters​
Parameter​
Type​
Description​
sellAds​
String​
Collection of sell ads. Schema is same as that of buy ads.​
buyAds​
String​
Collection of buy ads. ​

### Code Examples

```elixir
user and other use blacklisted each
```

```unknown
user has completed phone verification​
```

```unknown
user has completed email verification ​
```

```unknown
user. Valid values: NO_BLACK (No blacklist
```

```unknown
user blacklisted the other
```

```unknown
user for which ads are required​
```

---

---

**📄 Source: PDF Page 70**

> adId​
String​
Ad id​
> type​
String​
Ad price type. Valid values: ​
limit​
floating_market​
> side​
String​
Specifies the transaction side or direction. Valid values:​
buy​
sell​
> cryptoCurrency​
String​
Crypto currency symbol​
> fiatCurrency​
String​
Fiat currency symbol​
> minOrderSize​
String​
Order lower limit​
> maxOrderSize​
String​
Order upper limit​
> availableAmount​
String​
The available crypto quantity currently available for buying and 
selling​
> unitPrice​
String​
Unit price​
> priceMargin​
String​
The price margin ratio for floating type ads. Applicable only for 
ads with price type as floating price​
> minKycLevel​
String​
The minimum identity verification level of the taker. Valid 
values: 1,2,3​
> remark​
String​
Additional information or instructions for the ad for taker​
> createdTimestamp​
String​
Creation time of the ad​
> isHidden​
Boolea
n​
Specifies whether the ad is hidden or not​
> fiatPriceScale​
String​
Decimal places reserved for fiat currency​
> fiatPriceIncrement​
String​
Fiat currency increasing unit price gradient​
> fiatScale​
String​
Fiat Currency decimal places​
> cryptoScale​
String​
Crypto currency decimal places​
> minCompletedOrders​
String​
The minimum number of orders completed by the taker​
> maxCompletedOrders​
String​
The maximum number of orders completed by the taker​
> minSellOrders​
String​
The minimum number of sell orders completed by the taker​

---

---

**📄 Source: PDF Page 71**

> minCompletionRate​
String​
The minimum order completion rate of the taker​
> 
maxPaymentDurationInMi
nutes​
String​
The maximum time allowed for payment in minutes before 
timeout happens.​
> targetGroup​
String​
User target group for the ad. Valid values: ​
common​
certified​
diamond​
all​
> isSecurityLimitApplicable​
Boolea
n​
Specifies whether T+1 order​
> isProofRequired​
Boolea
n​
Specifies whether proof is required​
> verificationType​
String​
Specifies the verification type. Applies for Overseas Ads. Valid 
values:​
0 (no verification required)​
1 (verification required)​
paymentMethods​
String​
Collection of payment methods. Example: bank, aliPay, wxPay​
fiatSymbol​
String​
Fiat symbol. Examples：￥,$​
6.6 Get Followings​
Gets the following list for the merchant. ​
HTTP Request​
GET /api/v5/p2p/merchant/followings​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
pageIndex​
String​
Yes​
Current page index. Index starts from 1. Default value: 1​
pageLengt
h​
String​
Yes​
Size of each page. Default value: 20​

---

---

**📄 Source: PDF Page 72**

Response Parameters​
Parameter​
Type​
Description​
userId​
String​
Current page index. Index starts from 1. Default value: 1​
merchantId​
String​
Size of each page. Default value: 20​
nickname​
String​
Nick name of the merchant​
realName​
String​
Real name of the merchant​
avatarImage​
String​
Avatar image URL​
registeredTimestamp​
String​
Registration timestamp. Unix timestamp format in milliseconds​
userType​
String​
Type of the user. Valid values：common，certified，diamond​
kycLevel​
String​
The identity verification level of the user. Valid values: 1, 2, 3​
hasAlreadyTraded​
Boolean​
Specifies whether requester has traded with the following merchant​
hasOnlineAd​
Boolean​
Specifies whether the merchant has online ad​
6.7 Update following status​
Follow/unfollow a user.​
HTTP Request​
POST /api/v5/p2p/merchant/update-following-status​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
userId​
String​
Yes​
Id of the user who should be followed/unfollowed​
shouldFoll
ow​
Boolean​
Yes​
Specifies whether to follow the user. Valid values: true (to follow), 
false (un-follow)​
Response Parameters​
Parameter​
Type​
Description​

### Code Examples

```unknown
user. Valid values：common，certified，diamond​
```

```unknown
user who should be followed/unfollowed​
```

```unknown
user. Valid values: true (to follow),
```

```json
user. Valid values: 1, 2, 3​
```

---

---

**📄 Source: PDF Page 73**

userId​
String​
Id of the user who was followed/unfollowed​
6.8 Update Basic Information​
Update merchant's basic information.​
HTTP Request​
POST /api/v5/p2p/merchant/update-basic-info​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
avatarImag
e​
String​
Yes​
Merchant image URL​
description​
String​
Yes​
Description of the merchant​
7. Currency​
7.1 Get Fiat Currencies​
Retrieve supported Fiat Currencies for P2P.​
HTTP Request​
GET /api/v5/p2p/currency/fiat-currency-list​
Response Parameters​
Parameter​
Type​
Description​
currency​
String​
The fiat symbol. Example: USD​
name​
String​
Full name of currency​
symbol​
String​
Fiat currency symbol. Examples: ￥,$​
countryIcon​
String​
Country Icon​
isBlockTradeSupporte
d​
Boolean​
Specifies whether block trade is supported​
7.3 Get Currency Pair information​

### Code Examples

```unknown
user who was followed/unfollowed​
```

---

---

**📄 Source: PDF Page 74**

Retrieve supported Crypto currency pairs for a P2P fiat market.​
HTTP Request​
GET /api/v5/p2p/currency/currency-pair-list​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
fiatCurrenc
y​
String​
Yes​
The fiat currency symbol. Example: USD​
Response Parameters​
Parameter​
Type​
Description​
cryptoCurrency​
String​
The crypto currency symbol. Example: BTC​
fiatCurrency​
String​
The fiat currency symbol. Example: USD​
cryptoSymbol​
String​
Crypto currency symbol​
fiatName​
String​
Full name of fiat currency​
fiatSymbol​
String​
Fiat currency symbol. Examples: ￥,$​
fiatPriceScale​
String​
Decimal places reserved for fiat currency​
fiatPriceIncrement​
String​
Fiat currency increasing unit price gradient​
fiatScale​
String​
Fiat Currency decimal places​
cryptoScale​
String​
Crypto currency decimal places​
cryptoName​
String​
Full name of crypto currency​
countryIcon​
String​
Country icon​
8. Dispute​
8.1 Get Dispute Types​
Get available dispute types based on order.​
HTTP Request​

---

---

**📄 Source: PDF Page 75**

GET /api/v5/p2p/dispute/types​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Order Id​
side​
String​
No​
Specifies the transaction side or direction. Use buy to indicate a buy 
transaction, sell for a sell ​
transaction.​
Response Parameters​
Parameter​
Type​
Description​
disputeId​
String​
Dispute id​
subReason​
String​
Dispute subreason​
code​
String​
Dispute code​
hasSubType​
Boolean​
Specifies whether the dispute has sub-type​
subType​
String​
Collections of sub-types if dispute has any​
suggestions​
Array of 
Object​
Collection of suggestions. Schema is the same as the original object.​
> suggestText​
String​
Main suggestion message​
> children​
Array of 
String​
Sub-points for each suggestion​
videoSuggestion​
String​
Video proof request suggestion message​
imageSuggestion​
String​
Image proof request suggestion message​
isImageSubmissionNe
eded​
Boolean​
Indicates if the user needs to submit an image​
isRemarkSubmission
Needed​
Boolean​
Indicates if the user needs to submit a remark​
isVideoSubmissionNe
eded​
Boolean​
Indicates if the user needs to submit video​

### Code Examples

```unknown
user needs to submit an image​
```

```unknown
user needs to submit a remark​
```

```unknown
user needs to submit video​
```

---

---

**📄 Source: PDF Page 76**

Sample response:​
{
    "code": 0,
    "data": [
        {
            "sell": [
                {
                    "code": "14",
                    "disputeId": "SX14",
                    "hasSubType": true,
                    "imageSuggestion": "",
                    "isImageSubmissionNeeded": false,
                    "isRemarkSubmissionNeeded": true,
                    "isVideoSubmissionNeeded": true,
                    "subReason": "I received the payment but the order is 
canceled",
                    "subType": [
                        {
                            "code": "2",
                            "disputeId": "SX1402",
                            "hasSubType": false,
                            "imageSuggestion": "",
                            "isImageSubmissionNeeded": false,
                            "isRemarkSubmissionNeeded": true,
                            "isVideoSubmissionNeeded": true,
                            "subReason": "Transfer the crypto to the buyer",
                            "subType": [],
                            "suggestions": [
                                {
                                    "children": [],
                                    "suggestText": "Try reaching out to the 
other party to see if you can resolve the issue\n"
                                },
                                {
                                    "children": [],
                                    "suggestText": "Raise a dispute if you're 
unable to resolve it."
                                }
                            ],
                            "videoSuggestion": ""
                        },
                        {
                            "code": "3",
                            "disputeId": "SX1403",
                            "hasSubType": false,
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41

### Code Examples

```json
"code": 0,
    "data": [
        {
            "sell": [
                {
                    "code": "14",
                    "disputeId": "SX14",
                    "hasSubType": true,
                    "imageSuggestion": "",
                    "isImageSubmissionNeeded": false,
                    "isRemarkSubmissionNeeded": true,
                    "isVideoSubmissionNeeded": true,
                    "subReason": "I received the payment but the order is
```

```json
},
                                {
                                    "children": [],
                                    "suggestText": "Raise a dispute if you're
```

```json
}
                            ],
                            "videoSuggestion": ""
                        },
                        {
                            "code": "3",
                            "disputeId": "SX1403",
                            "hasSubType": false,
```

```json
"subType": [
                        {
                            "code": "2",
                            "disputeId": "SX1402",
                            "hasSubType": false,
                            "imageSuggestion": "",
                            "isImageSubmissionNeeded": false,
                            "isRemarkSubmissionNeeded": true,
                            "isVideoSubmissionNeeded": true,
                            "subReason": "Transfer the crypto to the buyer",
                            "subType": [],
                            "suggestions": [
                                {
                                    "children": [],
                                    "suggestText": "Try reaching out to the
"subType": [],
                            "suggestions": [
                                {
                                    "children": [],
                                    "suggestText": "Try reaching out to the
```

---

---

**📄 Source: PDF Page 77**

"imageSuggestion": "",
                            "isImageSubmissionNeeded": false,
                            "isRemarkSubmissionNeeded": true,
                            "isVideoSubmissionNeeded": true,
                            "subReason": "Customer Support to get account 
information for refund",
                            "subType": [],
                            "suggestions": [
                                {
                                    "children": [],
                                    "suggestText": "Try reaching out to the 
other party to see if you can resolve the issue\n"
                                },
                                {
                                    "children": [],
                                    "suggestText": "Raise a dispute if you're 
unable to resolve it."
                                }
                            ],
                            "videoSuggestion": ""
                        }
                    ],
                    "suggestions": [
                        {
                            "children": [],
                            "suggestText": "Try reaching out to the other 
party to see if you can resolve the issue\n"
                        },
                        {
                            "children": [],
                            "suggestText": "Raise a dispute if you're unable 
to resolve it."
                        }
                    ],
                    "videoSuggestion": ""
                }              
            ],
            "buy": [
                {
                    "code": "10",
                    "disputeId": "BX10",
                    "hasSubType": true,
                    "imageSuggestion": "",
                    "isImageSubmissionNeeded": false,
                    "isRemarkSubmissionNeeded": true,
                    "isVideoSubmissionNeeded": true,
                    "subReason": "I have paid but order is canceled",
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83

### Code Examples

```json
},
                                {
                                    "children": [],
                                    "suggestText": "Raise a dispute if you're
```

```json
}
                            ],
                            "videoSuggestion": ""
                        }
                    ],
                    "suggestions": [
                        {
                            "children": [],
                            "suggestText": "Try reaching out to the other
```

```json
},
                        {
                            "children": [],
                            "suggestText": "Raise a dispute if you're unable
```

```json
}
                    ],
                    "videoSuggestion": ""
                }              
            ],
            "buy": [
                {
                    "code": "10",
                    "disputeId": "BX10",
                    "hasSubType": true,
                    "imageSuggestion": "",
                    "isImageSubmissionNeeded": false,
                    "isRemarkSubmissionNeeded": true,
                    "isVideoSubmissionNeeded": true,
                    "subReason": "I have paid but order is canceled",
```

```json
"imageSuggestion": "",
                            "isImageSubmissionNeeded": false,
                            "isRemarkSubmissionNeeded": true,
                            "isVideoSubmissionNeeded": true,
                            "subReason": "Customer Support to get account
```

---

---

**📄 Source: PDF Page 78**

"subType": [
                        {
                            "code": "1",
                            "disputeId": "BX1001",
                            "hasSubType": false,
                            "imageSuggestion": "",
                            "isImageSubmissionNeeded": false,
                            "isRemarkSubmissionNeeded": true,
                            "isVideoSubmissionNeeded": true,
                            "subReason": "I can't contact the counterparty",
                            "subType": [],
                            "suggestions": [
                                {
                                    "children": [],
                                    "suggestText": "If you have made the 
payment but did not mark the order as paid, the seller has the obligation to 
refund you or accept your new order. Refund fee asked by the seller is at 
your own cost.\n"
                                },
                                {
                                    "children": [],
                                    "suggestText": "You can send ^the payment 
proof^ and reach a mutual agreement with the seller using our chat."
                                },
                                {
                                    "children": [],
                                    "suggestText": "If you can't reach the 
buyer, you can continue your dispute submission to our Customer Support."
                                }
                            ],
                            "videoSuggestion": "If you have already made 
payment for the order, please send us video proofs that contain the following 
information:\n\n1. Your bank account or payment platform used for the 
order.\n\n2. Your name and bank account number.\n\n3. The transaction date 
and the order amount.\n\n4. The P2P order page on the app (not on a separate 
bank statement).\n\n5. The seller's bank account number or email ID used for 
the order."
                        },                        
                    ],
                    "suggestions": [
                        {
                            "children": [],
                            "suggestText": "If you have made the payment but 
did not mark the order as paid, the seller has the obligation to refund you 
or accept your new order. Refund fee asked by the seller is at your own 
cost.\n"
                        },
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116

### Code Examples

```json
},
                                {
                                    "children": [],
                                    "suggestText": "You can send ^the payment
```

```json
},
                                {
                                    "children": [],
                                    "suggestText": "If you can't reach the
```

```json
},                        
                    ],
                    "suggestions": [
                        {
                            "children": [],
                            "suggestText": "If you have made the payment but
```

```json
"subType": [
                        {
                            "code": "1",
                            "disputeId": "BX1001",
                            "hasSubType": false,
                            "imageSuggestion": "",
                            "isImageSubmissionNeeded": false,
                            "isRemarkSubmissionNeeded": true,
                            "isVideoSubmissionNeeded": true,
                            "subReason": "I can't contact the counterparty",
                            "subType": [],
                            "suggestions": [
                                {
                                    "children": [],
                                    "suggestText": "If you have made the
```

```json
}
                            ],
                            "videoSuggestion": "If you have already made
```

---

---

**📄 Source: PDF Page 79**

{
                            "children": [],
                            "suggestText": "You can send ^the payment proof^ 
and reach a mutual agreement with the seller using our chat."
                        },
                        {
                            "children": [],
                            "suggestText": "If you can't reach the buyer, you 
can continue your dispute submission to our Customer Support."
                        }
                    ],
                    "videoSuggestion": "If you have already made payment for 
the order, please send us video proofs that contain the following 
information:\n\n1. Your bank account or payment platform used for the 
order.\n\n2. Your name and bank account number.\n\n3. The transaction date 
and the order amount.\n\n4. The P2P order page on the app (not on a separate 
bank statement).\n\n5. The seller's bank account number or email ID used for 
the order."
                }
            ],
            "appealUrge": []
        }
    ],
    "msg": ""
}
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
8.2 Create Dispute​
Creates dispute for an order.​
HTTP Request​
POST /api/v5/p2p/dispute/create​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Order Id for which dispute should be created​
disputeTyp
e​
String​
Yes​
Type of dispute​

### Code Examples

```json
{
                            "children": [],
                            "suggestText": "You can send ^the payment proof^
```

```json
},
                        {
                            "children": [],
                            "suggestText": "If you can't reach the buyer, you
```

```json
}
                    ],
                    "videoSuggestion": "If you have already made payment for
```

```json
}
            ],
            "appealUrge": []
        }
    ],
    "msg": ""
```

---

---

**📄 Source: PDF Page 80**

subDispute
Type​
String​
No​
Type of sub-dispute​
messageTe
xt​
String​
No​
Remark, necessary when dispute type is others​
imageUrls​
Array of 
String​
No​
Image proof urls​
videoUrls​
Array of 
String​
No​
Video proof urls​
disputeTyp
eUid​
String​
No​
Dispute type UID​
Response Parameters​
Parameter​
Type​
Description​
disputeId​
String​
Id of the created dispute​
8.3 Get Dispute Details​
Get dispute details including messages.​
HTTP Request​
GET /api/v5/p2p/dispute/dispute-details​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
orderId​
String​
Yes​
Id of the order for which dispute information is needed​
Response Parameters​
Parameter​
Type​
Description​
disputerSide​
String​
Specifies disputer side. Valid values: 0 (buyer), 1 (seller)​
isDisputer​
String​
Specifies whether the current user is the disputer. Valid values: true, 
false​

### Code Examples

```unknown
user is the disputer. Valid values: true,
```

---

---

**📄 Source: PDF Page 81**

disputeReason​
String​
Reason for the dispute​
disputeSubReason​
String​
Sub-reason for the dispute​
userLastReadTimesta
mp​
String​
Last read timestamp of the user​
messages​
Array of 
Object​
Collections of message details​
> message​
String​
Message text​
> sender​
String​
Sender of the message. Valid values: 0 (Self), 1 (Customer Support), 
2 (Counterparty)​
> senderName​
String​
Name of the message sender​
> imageUrls​
String​
Image urls​
> videoUrls​
String​
Video urls​
> timestamp​
String​
Message sent timestamp. Unix timestamp format in milliseconds​
Sample Response:​
{
    "code": 0,
    "data": [
        {
            "disputeReason": "I received the payment but the order is 
canceled",
            "disputeSubReason": "Transfer the crypto to the buyer",
            "disputerSide": "1",
            "isDisputer": true,
            "messages": [
                {
                    "imageUrls": [],
                    "message": "",
                    "sender": "0",
                    "senderName": "",
                    "timestamp": "1721269451000",
                    "translatedMessage": "",
                    "videoUrls": []
                },
                {
                    "imageUrls": [],
                    "message": "",
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

### Code Examples

```json
"code": 0,
    "data": [
        {
            "disputeReason": "I received the payment but the order is
```

```json
"disputeSubReason": "Transfer the crypto to the buyer",
            "disputerSide": "1",
            "isDisputer": true,
            "messages": [
                {
                    "imageUrls": [],
                    "message": "",
                    "sender": "0",
                    "senderName": "",
                    "timestamp": "1721269451000",
                    "translatedMessage": "",
                    "videoUrls": []
                },
                {
                    "imageUrls": [],
                    "message": "",
```

```unknown
userLastReadTimesta
```

---

---

**📄 Source: PDF Page 82**

"sender": "1",
                    "senderName": "abcd",
                    "timestamp": "1721269451000",
                    "translatedMessage": "",
                    "videoUrls": [
                        
"https://static.coinall.ltd/cdn/oksupport/c2c/20240718_a8005793-9826-4c95-
b25d.mp4"
                    ]
                },
                {
                    "imageUrls": [],
                    "message": "",
                    "sender": "0",
                    "senderName": "",
                    "timestamp": "1721269431000",
                    "translatedMessage": "",
                    "videoUrls": []
                },
                {
                    "imageUrls": [],
                    "message": "",
                    "sender": "1",
                    "senderName": "test4fiat2",
                    "timestamp": "1721269431000",
                    "translatedMessage": "",
                    "videoUrls": [
                        
"https://static.coinall.ltd/cdn/oksupport/c2c/20240718_f42ce0bb-a2c0-4c43-
9e2.mp4"
                    ]
                }
            ]
        }
    ],
    "msg": ""
}
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
8.4 Send message​
Send a message for the dispute.​
HTTP Request​
POST /api/v5/p2p/dispute/sendMessage​
Request Parameters​

### Code Examples

```json
]
                },
                {
                    "imageUrls": [],
                    "message": "",
                    "sender": "0",
                    "senderName": "",
                    "timestamp": "1721269431000",
                    "translatedMessage": "",
                    "videoUrls": []
                },
                {
                    "imageUrls": [],
                    "message": "",
                    "sender": "1",
                    "senderName": "test4fiat2",
                    "timestamp": "1721269431000",
                    "translatedMessage": "",
                    "videoUrls": [
```

```json
"sender": "1",
                    "senderName": "abcd",
                    "timestamp": "1721269451000",
                    "translatedMessage": "",
                    "videoUrls": [
```

```json
]
                }
            ]
        }
    ],
    "msg": ""
```

---

---

**📄 Source: PDF Page 83**

Parameter​
Type​
Requir
ed​
Description​
orderId​
String​
Yes​
Order Id​
message​
String​
No​
Message text​
imageUrls​
Array of String​
No​
User-uploaded image URLs​
videoUrls​
Array of String​
No​
User-uploaded video URLs​
Response Parameters​
Parameter​
Type​
Description​
id​
String​
Order Id for which evidence got updated​
8.5 Cancel Dispute​
Cancels the dispute.
HTTP Request​
POST /api/v5/p2p/dispute/cancel​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​
orderId​
String​
Yes​
Order Id​
Response Parameters​
Parameter​
Type​
Description​
orderId​
String​
Id of the order for which dispute got cancelled​
9. Chat​
9.1 Get Chat history for order​

---

---

**📄 Source: PDF Page 84**

Get chat history based on order. The messages are ordered from the latest to the oldest. System-
generated messages are not returned.​
HTTP Request​
GET /api/v5/p2p/chat/history​
Request Parameters​
Parameter​
Type​
Require
d​
Description​
orderId​
String​
Optional​
•
If the orderId  is specified, the API will return all chat 
messages related to that specific order. Note that once the order 
is completed, no further chat messages can be retrieved for that 
order.​
•
 If the orderId  is not provided, the API will return all available 
chat messages between the counterparty​
lastMessag
eSequence​
String​
No​
Specifies the last message sequence number. Eg: "123"​
This param is required if messages are required to be fetched 
backword.​
pageSize​
String​
Yes​
Specifies the number of messages to be retrieved.​
Response Parameters​
Parameter​
Type​
Description​
sentTimestamp​
String​
Epoch timestamp for the message sent time​
isSentBySelf​
String​
Specifies whether requestor is the sender as well​
content​
String​
Text of the content. Eg: "Hello"​
contentUrl​
Boolean​
If the message is of a media type (like an image/video, etc.), the URL 
is returned. Content present at this URL can be retrieved for 30 days 
from the time the content is uploaded.​
lastMessageSequence​
String​
The sequence number of the message. Eg: "123"
9.2 Send message​
Send message for the order to the counterparty.​

### Code Examples

```unknown
required if messages are required to be fetched
```

---

---

**📄 Source: PDF Page 85**

HTTP Request​
POST /api/v5/p2p/chat/send-message​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​
orderId​
String​
Yes​
Order Id. Eg: "12345"​
content​
String​
No​
Text of the content. Eg: "Hello"​
contentUrl​
String​
No​
If the message is of a media type (like an image/video, etc.), 
then specify the url. URL can be generated by calling file upload 
API.​
contentType​
String​
Yes​
Type of content.​
101 => Text​
102 => Image​
112 => Video​
Response Parameters​
Parameter​
Type​
Description​
isSentSuccessfully​
Boolean​
Specifies whether the message was sent successfully to the other 
user or not.​
10. File​
10.1 Upload file​
HTTP Request​
POST /api/v5/p2p/file/upload​
The input is multipart file.​
Request Parameters​
Parameter​
Type​
Requir
ed​
Description​

---

---

**📄 Source: PDF Page 86**

file​
Multipa
rt​
Yes​
Response Parameters​
Parameter​
Type​
Description​
path​
String​
Path of the uploaded file. Eg: "http://abc.com/xyz"​

---

