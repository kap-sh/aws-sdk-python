"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchConstraintType``."""

from typing import Literal, TypeAlias, cast

GeoMatchConstraintType: TypeAlias = Literal["Country",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchConstraintType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GeoMatchConstraintType:
    return cast(GeoMatchConstraintType, data)
