"""Generated from Smithy shape ``com.amazonaws.emr#ListReleaseLabelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.string
    import aws_sdk_emr.types.string_list


class ListReleaseLabelsOutput(TypedDict, closed=True):
    release_labels: NotRequired["aws_sdk_emr.types.string_list.StringList"]
    """<p>The returned release labels.</p>"""
    next_token: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>Used to paginate the next page of results if specified in the next <code>ListReleaseLabels</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReleaseLabelsOutput) -> dict:
    out: dict = {}
    if "release_labels" in value:
        import aws_sdk_emr.types.string_list

        out["ReleaseLabels"] = aws_sdk_emr.types.string_list.serialize_aws_json_1_1(
            value["release_labels"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReleaseLabelsOutput:
    out: ListReleaseLabelsOutput = {}  # type: ignore[typeddict-item]
    if "ReleaseLabels" in data:
        import aws_sdk_emr.types.string_list

        out["release_labels"] = aws_sdk_emr.types.string_list.deserialize_aws_json_1_1(
            data["ReleaseLabels"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
