"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListEnvironmentVpcsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.environment_vpcs
    import capo_migration_hub_refactor_spaces.types.next_token


class ListEnvironmentVpcsResponse(TypedDict, closed=True):
    environment_vpc_list: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_vpcs.EnvironmentVpcs"
    ]
    """<p>The list of <code>EnvironmentVpc</code> objects. </p>"""
    next_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentVpcsResponse) -> dict:
    out: dict = {}
    if "environment_vpc_list" in value:
        import capo_migration_hub_refactor_spaces.types.environment_vpcs

        out["EnvironmentVpcList"] = (
            capo_migration_hub_refactor_spaces.types.environment_vpcs.serialize_json(
                value["environment_vpc_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentVpcsResponse:
    out: ListEnvironmentVpcsResponse = {}  # type: ignore[typeddict-item]
    if "EnvironmentVpcList" in data:
        import capo_migration_hub_refactor_spaces.types.environment_vpcs

        out["environment_vpc_list"] = (
            capo_migration_hub_refactor_spaces.types.environment_vpcs.deserialize_json(
                data["EnvironmentVpcList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
