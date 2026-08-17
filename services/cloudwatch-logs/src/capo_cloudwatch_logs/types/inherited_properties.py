"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#InheritedProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.inherited_property

InheritedProperties: TypeAlias = list[
    "capo_cloudwatch_logs.types.inherited_property.InheritedProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InheritedProperties) -> list:
    import capo_cloudwatch_logs.types.inherited_property

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.inherited_property.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InheritedProperties:
    import capo_cloudwatch_logs.types.inherited_property

    out: InheritedProperties = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.inherited_property.deserialize_aws_json_1_1(item)
        )
    return out
