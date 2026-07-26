"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchInstanceTypeLimitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.limits_by_role


class DescribeElasticsearchInstanceTypeLimitsResponse(TypedDict, closed=True):
    limits_by_role: NotRequired[
        "capo_elasticsearch_service.types.limits_by_role.LimitsByRole"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchInstanceTypeLimitsResponse) -> dict:
    out: dict = {}
    if "limits_by_role" in value:
        import capo_elasticsearch_service.types.limits_by_role

        out["LimitsByRole"] = (
            capo_elasticsearch_service.types.limits_by_role.serialize_json(
                value["limits_by_role"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchInstanceTypeLimitsResponse:
    out: DescribeElasticsearchInstanceTypeLimitsResponse = {}  # type: ignore[typeddict-item]
    if "LimitsByRole" in data:
        import capo_elasticsearch_service.types.limits_by_role

        out["limits_by_role"] = (
            capo_elasticsearch_service.types.limits_by_role.deserialize_json(
                data["LimitsByRole"]
            )
        )
    return out
