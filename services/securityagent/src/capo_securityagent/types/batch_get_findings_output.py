"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetFindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.finding_id_list
    import capo_securityagent.types.finding_list


class BatchGetFindingsOutput(TypedDict, closed=True):
    findings: NotRequired["capo_securityagent.types.finding_list.FindingList"]
    """<p>The list of findings that were found.</p>"""
    not_found: NotRequired["capo_securityagent.types.finding_id_list.FindingIdList"]
    """<p>The list of finding identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsOutput) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_securityagent.types.finding_list

        out["findings"] = capo_securityagent.types.finding_list.serialize_json(
            value["findings"]
        )
    if "not_found" in value:
        import capo_securityagent.types.finding_id_list

        out["notFound"] = capo_securityagent.types.finding_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetFindingsOutput:
    out: BatchGetFindingsOutput = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import capo_securityagent.types.finding_list

        out["findings"] = capo_securityagent.types.finding_list.deserialize_json(
            data["findings"]
        )
    if "notFound" in data:
        import capo_securityagent.types.finding_id_list

        out["not_found"] = capo_securityagent.types.finding_id_list.deserialize_json(
            data["notFound"]
        )
    return out
