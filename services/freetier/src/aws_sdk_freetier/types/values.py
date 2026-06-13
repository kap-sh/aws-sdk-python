"""Generated from Smithy shape ``com.amazonaws.freetier#Values``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_freetier.types.value

Values: TypeAlias = list["aws_sdk_freetier.types.value.Value"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Values) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Values:
    return list(data)
