"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetFindingDetailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.finding_arn_list


class BatchGetFindingDetailsRequest(TypedDict, closed=True):
    finding_arns: "capo_inspector2.types.finding_arn_list.FindingArnList"
    """<p>A list of finding ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingDetailsRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.finding_arn_list

    out["findingArns"] = capo_inspector2.types.finding_arn_list.serialize_json(
        value["finding_arns"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetFindingDetailsRequest:
    out: BatchGetFindingDetailsRequest = {}  # type: ignore[typeddict-item]
    if "findingArns" in data:
        import capo_inspector2.types.finding_arn_list

        out["finding_arns"] = capo_inspector2.types.finding_arn_list.deserialize_json(
            data["findingArns"]
        )
    else:
        raise DeserializationError(
            "BatchGetFindingDetailsRequest.finding_arns required"
        )
    return out
