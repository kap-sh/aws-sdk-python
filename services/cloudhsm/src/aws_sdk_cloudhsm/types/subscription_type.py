"""Generated from Smithy shape ``com.amazonaws.cloudhsm#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm.errors import DeserializationError

"""<p>Specifies the type of subscription for the HSM.</p> <ul> <li> <p> <b>PRODUCTION</b> - The HSM is being used in a production environment.</p> </li> <li> <p> <b>TRIAL</b> - The HSM is being used in a product trial.</p> </li> </ul>"""
SubscriptionType: TypeAlias = Literal["PRODUCTION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PRODUCTION",))


def serialize_aws_json_1_1(value: SubscriptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionType value: {data!r}")
    return cast(SubscriptionType, data)
