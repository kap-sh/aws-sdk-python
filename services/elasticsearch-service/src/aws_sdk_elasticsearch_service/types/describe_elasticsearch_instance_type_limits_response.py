"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchInstanceTypeLimitsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.limits_by_role


class DescribeElasticsearchInstanceTypeLimitsResponse(TypedDict):
    limits_by_role: NotRequired[
        "aws_sdk_elasticsearch_service.types.limits_by_role.LimitsByRole"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchInstanceTypeLimitsResponse) -> dict:
    out: dict = {}
    if "limits_by_role" in value:
        import aws_sdk_elasticsearch_service.types.limits_by_role

        out["LimitsByRole"] = (
            aws_sdk_elasticsearch_service.types.limits_by_role.serialize_json(
                value["limits_by_role"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchInstanceTypeLimitsResponse:
    out: DescribeElasticsearchInstanceTypeLimitsResponse = {}  # type: ignore[typeddict-item]
    if "LimitsByRole" in data:
        import aws_sdk_elasticsearch_service.types.limits_by_role

        out["limits_by_role"] = (
            aws_sdk_elasticsearch_service.types.limits_by_role.deserialize_json(
                data["LimitsByRole"]
            )
        )
    return out
