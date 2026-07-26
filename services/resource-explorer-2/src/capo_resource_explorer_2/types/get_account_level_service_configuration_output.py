"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetAccountLevelServiceConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.org_configuration


class GetAccountLevelServiceConfigurationOutput(TypedDict, closed=True):
    org_configuration: NotRequired[
        "capo_resource_explorer_2.types.org_configuration.OrgConfiguration"
    ]
    """<p>Details about the organization, and whether configuration is <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountLevelServiceConfigurationOutput) -> dict:
    out: dict = {}
    if "org_configuration" in value:
        import capo_resource_explorer_2.types.org_configuration

        out["OrgConfiguration"] = (
            capo_resource_explorer_2.types.org_configuration.serialize_json(
                value["org_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAccountLevelServiceConfigurationOutput:
    out: GetAccountLevelServiceConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "OrgConfiguration" in data:
        import capo_resource_explorer_2.types.org_configuration

        out["org_configuration"] = (
            capo_resource_explorer_2.types.org_configuration.deserialize_json(
                data["OrgConfiguration"]
            )
        )
    return out
