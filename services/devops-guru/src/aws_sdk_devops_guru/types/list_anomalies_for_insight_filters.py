"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListAnomaliesForInsightFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.service_collection


class ListAnomaliesForInsightFilters(TypedDict):
    service_collection: NotRequired[
        "aws_sdk_devops_guru.types.service_collection.ServiceCollection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomaliesForInsightFilters) -> dict:
    out: dict = {}
    if "service_collection" in value:
        import aws_sdk_devops_guru.types.service_collection

        out["ServiceCollection"] = (
            aws_sdk_devops_guru.types.service_collection.serialize_json(
                value["service_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAnomaliesForInsightFilters:
    out: ListAnomaliesForInsightFilters = {}  # type: ignore[typeddict-item]
    if "ServiceCollection" in data:
        import aws_sdk_devops_guru.types.service_collection

        out["service_collection"] = (
            aws_sdk_devops_guru.types.service_collection.deserialize_json(
                data["ServiceCollection"]
            )
        )
    return out
