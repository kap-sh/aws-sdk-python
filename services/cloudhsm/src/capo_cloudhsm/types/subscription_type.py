"""Generated from Smithy shape ``com.amazonaws.cloudhsm#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the type of subscription for the HSM.</p> <ul> <li> <p> <b>PRODUCTION</b> - The HSM is being used in a production environment.</p> </li> <li> <p> <b>TRIAL</b> - The HSM is being used in a product trial.</p> </li> </ul>"""
SubscriptionType: TypeAlias = Literal["PRODUCTION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriptionType:
    return cast(SubscriptionType, data)
