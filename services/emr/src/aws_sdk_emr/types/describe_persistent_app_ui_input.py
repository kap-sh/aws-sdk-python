"""Generated from Smithy shape ``com.amazonaws.emr#DescribePersistentAppUIInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_max_len256


class DescribePersistentAppUIInput(TypedDict, closed=True):
    persistent_app_ui_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier for the persistent application user interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePersistentAppUIInput) -> dict:
    out: dict = {}
    if "persistent_app_ui_id" in value:
        out["PersistentAppUIId"] = value["persistent_app_ui_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePersistentAppUIInput:
    out: DescribePersistentAppUIInput = {}  # type: ignore[typeddict-item]
    if "PersistentAppUIId" in data:
        out["persistent_app_ui_id"] = data["PersistentAppUIId"]
    return out
