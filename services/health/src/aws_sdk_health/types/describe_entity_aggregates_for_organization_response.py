"""Generated from Smithy shape ``com.amazonaws.health#DescribeEntityAggregatesForOrganizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.organization_entity_aggregates_list


class DescribeEntityAggregatesForOrganizationResponse(TypedDict):
    organization_entity_aggregates: NotRequired[
        "aws_sdk_health.types.organization_entity_aggregates_list.OrganizationEntityAggregatesList"
    ]
    """<p>The list of entity aggregates for each of the specified accounts that are affected by each of the specified events.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeEntityAggregatesForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "organization_entity_aggregates" in value:
        import aws_sdk_health.types.organization_entity_aggregates_list

        out["organizationEntityAggregates"] = (
            aws_sdk_health.types.organization_entity_aggregates_list.serialize_aws_json_1_1(
                value["organization_entity_aggregates"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeEntityAggregatesForOrganizationResponse:
    out: DescribeEntityAggregatesForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if "organizationEntityAggregates" in data:
        import aws_sdk_health.types.organization_entity_aggregates_list

        out["organization_entity_aggregates"] = (
            aws_sdk_health.types.organization_entity_aggregates_list.deserialize_aws_json_1_1(
                data["organizationEntityAggregates"]
            )
        )
    return out
