"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetFindingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.finding_id_list
    import aws_sdk_securityagent.types.finding_list


class BatchGetFindingsOutput(TypedDict):
    findings: NotRequired["aws_sdk_securityagent.types.finding_list.FindingList"]
    """<p>The list of findings that were found.</p>"""
    not_found: NotRequired["aws_sdk_securityagent.types.finding_id_list.FindingIdList"]
    """<p>The list of finding identifiers that were not found.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFindingsOutput) -> dict:
    out: dict = {}
    if "findings" in value:
        import aws_sdk_securityagent.types.finding_list

        out["findings"] = aws_sdk_securityagent.types.finding_list.serialize_json(
            value["findings"]
        )
    if "not_found" in value:
        import aws_sdk_securityagent.types.finding_id_list

        out["notFound"] = aws_sdk_securityagent.types.finding_id_list.serialize_json(
            value["not_found"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetFindingsOutput:
    out: BatchGetFindingsOutput = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_securityagent.types.finding_list

        out["findings"] = aws_sdk_securityagent.types.finding_list.deserialize_json(
            data["findings"]
        )
    if "notFound" in data:
        import aws_sdk_securityagent.types.finding_id_list

        out["not_found"] = aws_sdk_securityagent.types.finding_id_list.deserialize_json(
            data["notFound"]
        )
    return out
