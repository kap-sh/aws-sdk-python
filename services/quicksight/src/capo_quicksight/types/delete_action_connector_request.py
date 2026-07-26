"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteActionConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DeleteActionConnectorRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID that contains the action connector to delete.</p>"""
    action_connector_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The unique identifier of the action connector to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteActionConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteActionConnectorRequest:
    out: DeleteActionConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
