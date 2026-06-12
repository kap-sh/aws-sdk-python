"""Generated from Smithy shape ``com.amazonaws.dataexchange#UpdateRevisionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__boolean
    import aws_sdk_dataexchange.types.__string_min0_max16384
    import aws_sdk_dataexchange.types.id


class UpdateRevisionRequest(TypedDict):
    comment: NotRequired[
        "aws_sdk_dataexchange.types.__string_min0_max16384.__stringMin0Max16384"
    ]
    """<p>An optional comment about the revision.</p>"""
    data_set_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    finalized: "aws_sdk_dataexchange.types.__boolean.__boolean"
    """<p>Finalizing a revision tells AWS Data Exchange that your changes to the assets in the revision are complete. After it's in this read-only state, you can publish the revision to your products.</p>"""
    revision_id: "aws_sdk_dataexchange.types.id.Id"
    """<p>The unique identifier for a revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRevisionRequest) -> dict:
    out: dict = {}
    if "comment" in value:
        out["Comment"] = value["comment"]
    out["Finalized"] = value.get("finalized", False)
    return out


def deserialize_json(data: dict) -> UpdateRevisionRequest:
    out: UpdateRevisionRequest = {}  # type: ignore[typeddict-item]
    if "Comment" in data:
        out["comment"] = data["Comment"]
    if "Finalized" in data:
        out["finalized"] = data["Finalized"]
    else:
        out["finalized"] = False
    return out
