"""Generated from Smithy shape ``com.amazonaws.kendra#FacetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.facet

FacetList: TypeAlias = list["aws_sdk_kendra.types.facet.Facet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FacetList) -> list:
    import aws_sdk_kendra.types.facet

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.facet.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FacetList:
    import aws_sdk_kendra.types.facet

    out: FacetList = []
    for item in data:
        out.append(aws_sdk_kendra.types.facet.deserialize_aws_json_1_1(item))
    return out
