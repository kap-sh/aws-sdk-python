"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingHistoryUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class FindingHistoryUpdate(TypedDict):
    updated_field: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The ASFF field that changed during the finding change event. </p>"""
    old_value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The value of the ASFF field before the finding change event. </p>"""
    new_value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p> The value of the ASFF field after the finding change event. To preserve storage and readability, Security Hub CSPM omits this value if <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryRecord.html\"> <code>FindingHistoryRecord</code> </a> exceeds database limits. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingHistoryUpdate) -> dict:
    out: dict = {}
    if "updated_field" in value:
        out["UpdatedField"] = value["updated_field"]
    if "old_value" in value:
        out["OldValue"] = value["old_value"]
    if "new_value" in value:
        out["NewValue"] = value["new_value"]
    return out


def deserialize_json(data: dict) -> FindingHistoryUpdate:
    out: FindingHistoryUpdate = {}  # type: ignore[typeddict-item]
    if "UpdatedField" in data:
        out["updated_field"] = data["UpdatedField"]
    if "OldValue" in data:
        out["old_value"] = data["OldValue"]
    if "NewValue" in data:
        out["new_value"] = data["NewValue"]
    return out
