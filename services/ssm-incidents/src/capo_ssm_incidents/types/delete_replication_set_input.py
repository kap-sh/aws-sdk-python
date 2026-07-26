"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteReplicationSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn


class DeleteReplicationSetInput(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set you're deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReplicationSetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReplicationSetInput:
    out: DeleteReplicationSetInput = {}  # type: ignore[typeddict-item]
    return out
