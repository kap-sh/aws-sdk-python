"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactMethodsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.contact_method

ContactMethodsList: TypeAlias = list[
    "capo_lightsail.types.contact_method.ContactMethod"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactMethodsList) -> list:
    import capo_lightsail.types.contact_method

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.contact_method.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContactMethodsList:
    import capo_lightsail.types.contact_method

    out: ContactMethodsList = []
    for item in data:
        out.append(capo_lightsail.types.contact_method.deserialize_aws_json_1_1(item))
    return out
