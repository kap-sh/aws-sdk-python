"""Generated from Smithy shape ``com.amazonaws.deadline#PathMappingRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.path_mapping_rule

PathMappingRules: TypeAlias = list[
    "aws_sdk_deadline.types.path_mapping_rule.PathMappingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: PathMappingRules) -> list:
    import aws_sdk_deadline.types.path_mapping_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_deadline.types.path_mapping_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> PathMappingRules:
    import aws_sdk_deadline.types.path_mapping_rule

    out: PathMappingRules = []
    for item in data:
        out.append(aws_sdk_deadline.types.path_mapping_rule.deserialize_json(item))
    return out
