"""Generated from Smithy shape ``com.amazonaws.backup#ListTieringConfigurationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.tiering_configurations_list


class ListTieringConfigurationsOutput(TypedDict):
    tiering_configurations: NotRequired[
        "aws_sdk_backup.types.tiering_configurations_list.TieringConfigurationsList"
    ]
    """<p>An array of tiering configurations returned by the <code>ListTieringConfigurations</code> call.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTieringConfigurationsOutput) -> dict:
    out: dict = {}
    if "tiering_configurations" in value:
        import aws_sdk_backup.types.tiering_configurations_list

        out["TieringConfigurations"] = (
            aws_sdk_backup.types.tiering_configurations_list.serialize_json(
                value["tiering_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTieringConfigurationsOutput:
    out: ListTieringConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "TieringConfigurations" in data:
        import aws_sdk_backup.types.tiering_configurations_list

        out["tiering_configurations"] = (
            aws_sdk_backup.types.tiering_configurations_list.deserialize_json(
                data["TieringConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
