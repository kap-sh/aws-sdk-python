"""Generated from Smithy shape ``com.amazonaws.support#DescribeSeverityLevelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.language


class DescribeSeverityLevelsRequest(TypedDict):
    language: NotRequired["aws_sdk_support.types.language.Language"]
    """<p>The language in which Amazon Web Services Support handles the case. Amazon Web Services Support currently supports Chinese (“zh”), English (\"en\"), Japanese (\"ja\") and Korean (“ko”). You must specify the ISO 639-1 code for the <code>language</code> parameter if you want support in that language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSeverityLevelsRequest) -> dict:
    out: dict = {}
    if "language" in value:
        out["language"] = value["language"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSeverityLevelsRequest:
    out: DescribeSeverityLevelsRequest = {}  # type: ignore[typeddict-item]
    if "language" in data:
        out["language"] = data["language"]
    return out
