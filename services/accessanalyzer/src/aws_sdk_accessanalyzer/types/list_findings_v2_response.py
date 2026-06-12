"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListFindingsV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.findings_list_v2
    import aws_sdk_accessanalyzer.types.token


class ListFindingsV2Response(TypedDict):
    findings: "aws_sdk_accessanalyzer.types.findings_list_v2.FindingsListV2"
    """<p>A list of findings retrieved from the analyzer that match the filter criteria specified, if any.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingsV2Response) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.findings_list_v2

    out["findings"] = aws_sdk_accessanalyzer.types.findings_list_v2.serialize_json(
        value["findings"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingsV2Response:
    out: ListFindingsV2Response = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_accessanalyzer.types.findings_list_v2

        out["findings"] = (
            aws_sdk_accessanalyzer.types.findings_list_v2.deserialize_json(
                data["findings"]
            )
        )
    else:
        raise DeserializationError("ListFindingsV2Response.findings required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
