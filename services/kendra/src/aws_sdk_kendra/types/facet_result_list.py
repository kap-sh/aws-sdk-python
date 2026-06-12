"""Generated from Smithy shape ``com.amazonaws.kendra#FacetResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.facet_result

FacetResultList: TypeAlias = list["aws_sdk_kendra.types.facet_result.FacetResult"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FacetResultList) -> list:
    import aws_sdk_kendra.types.facet_result

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.facet_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FacetResultList:
    import aws_sdk_kendra.types.facet_result

    out: FacetResultList = []
    for item in data:
        out.append(aws_sdk_kendra.types.facet_result.deserialize_aws_json_1_1(item))
    return out
