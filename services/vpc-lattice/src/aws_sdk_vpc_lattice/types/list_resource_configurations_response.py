"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_configuration_summary_list


class ListResourceConfigurationsResponse(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_configuration_summary_list.ResourceConfigurationSummaryList"
    ]
    """<p>Information about the resource configurations.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceConfigurationsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_vpc_lattice.types.resource_configuration_summary_list

        out["items"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_summary_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceConfigurationsResponse:
    out: ListResourceConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_vpc_lattice.types.resource_configuration_summary_list

        out["items"] = (
            aws_sdk_vpc_lattice.types.resource_configuration_summary_list.deserialize_json(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
