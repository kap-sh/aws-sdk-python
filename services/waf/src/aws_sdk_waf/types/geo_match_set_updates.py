"""Generated from Smithy shape ``com.amazonaws.waf#GeoMatchSetUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_waf.types.geo_match_set_update

GeoMatchSetUpdates: TypeAlias = list[
    "aws_sdk_waf.types.geo_match_set_update.GeoMatchSetUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeoMatchSetUpdates) -> list:
    import aws_sdk_waf.types.geo_match_set_update

    out: list = []
    for item in value:
        out.append(aws_sdk_waf.types.geo_match_set_update.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> GeoMatchSetUpdates:
    import aws_sdk_waf.types.geo_match_set_update

    out: GeoMatchSetUpdates = []
    for item in data:
        out.append(
            aws_sdk_waf.types.geo_match_set_update.deserialize_aws_json_1_1(item)
        )
    return out
