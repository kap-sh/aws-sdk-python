"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.configurations_list


class ListConfigurationsOutput(TypedDict, closed=True):
    configurations_list: NotRequired[
        "aws_sdk_ssm_quicksetup.types.configurations_list.ConfigurationsList"
    ]
    """<p>An array of configurations.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationsOutput) -> dict:
    out: dict = {}
    if "configurations_list" in value:
        import aws_sdk_ssm_quicksetup.types.configurations_list

        out["ConfigurationsList"] = (
            aws_sdk_ssm_quicksetup.types.configurations_list.serialize_json(
                value["configurations_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationsOutput:
    out: ListConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "ConfigurationsList" in data:
        import aws_sdk_ssm_quicksetup.types.configurations_list

        out["configurations_list"] = (
            aws_sdk_ssm_quicksetup.types.configurations_list.deserialize_json(
                data["ConfigurationsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
