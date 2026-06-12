"""Generated from Smithy shape ``com.amazonaws.devopsguru#SearchOrganizationInsightsFilters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.insight_severities
    import aws_sdk_devops_guru.types.insight_statuses
    import aws_sdk_devops_guru.types.resource_collection
    import aws_sdk_devops_guru.types.service_collection


class SearchOrganizationInsightsFilters(TypedDict):
    severities: NotRequired[
        "aws_sdk_devops_guru.types.insight_severities.InsightSeverities"
    ]
    """<p> An array of severity values used to search for insights. </p>"""
    statuses: NotRequired["aws_sdk_devops_guru.types.insight_statuses.InsightStatuses"]
    """<p> An array of status values used to search for insights. </p>"""
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection.ResourceCollection"
    ]
    service_collection: NotRequired[
        "aws_sdk_devops_guru.types.service_collection.ServiceCollection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SearchOrganizationInsightsFilters) -> dict:
    out: dict = {}
    if "severities" in value:
        import aws_sdk_devops_guru.types.insight_severities

        out["Severities"] = aws_sdk_devops_guru.types.insight_severities.serialize_json(
            value["severities"]
        )
    if "statuses" in value:
        import aws_sdk_devops_guru.types.insight_statuses

        out["Statuses"] = aws_sdk_devops_guru.types.insight_statuses.serialize_json(
            value["statuses"]
        )
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "service_collection" in value:
        import aws_sdk_devops_guru.types.service_collection

        out["ServiceCollection"] = (
            aws_sdk_devops_guru.types.service_collection.serialize_json(
                value["service_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchOrganizationInsightsFilters:
    out: SearchOrganizationInsightsFilters = {}  # type: ignore[typeddict-item]
    if "Severities" in data:
        import aws_sdk_devops_guru.types.insight_severities

        out["severities"] = (
            aws_sdk_devops_guru.types.insight_severities.deserialize_json(
                data["Severities"]
            )
        )
    if "Statuses" in data:
        import aws_sdk_devops_guru.types.insight_statuses

        out["statuses"] = aws_sdk_devops_guru.types.insight_statuses.deserialize_json(
            data["Statuses"]
        )
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if "ServiceCollection" in data:
        import aws_sdk_devops_guru.types.service_collection

        out["service_collection"] = (
            aws_sdk_devops_guru.types.service_collection.deserialize_json(
                data["ServiceCollection"]
            )
        )
    return out
