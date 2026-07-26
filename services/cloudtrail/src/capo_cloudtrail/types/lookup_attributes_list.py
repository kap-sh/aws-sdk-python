"""Generated from Smithy shape ``com.amazonaws.cloudtrail#LookupAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.lookup_attribute

LookupAttributesList: TypeAlias = list[
    "capo_cloudtrail.types.lookup_attribute.LookupAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupAttributesList) -> list:
    import capo_cloudtrail.types.lookup_attribute

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.lookup_attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LookupAttributesList:
    import capo_cloudtrail.types.lookup_attribute

    out: LookupAttributesList = []
    for item in data:
        out.append(
            capo_cloudtrail.types.lookup_attribute.deserialize_aws_json_1_1(item)
        )
    return out
