"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DeleteSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class DeleteSchemaRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the development schema. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaRequest:
    out: DeleteSchemaRequest = {}  # type: ignore[typeddict-item]
    return out
