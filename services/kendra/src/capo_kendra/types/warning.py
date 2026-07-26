"""Generated from Smithy shape ``com.amazonaws.kendra#Warning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.warning_code
    import capo_kendra.types.warning_message


class Warning(TypedDict, closed=True):
    message: NotRequired["capo_kendra.types.warning_message.WarningMessage"]
    """<p>The message that explains the problem with the query.</p>"""
    code: NotRequired["capo_kendra.types.warning_code.WarningCode"]
    """<p>The code used to show the type of warning for the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Warning) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        import capo_kendra.types.warning_code

        out["Code"] = capo_kendra.types.warning_code.serialize_aws_json_1_1(
            value["code"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Warning:
    out: Warning = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        import capo_kendra.types.warning_code

        out["code"] = capo_kendra.types.warning_code.deserialize_aws_json_1_1(
            data["Code"]
        )
    return out
