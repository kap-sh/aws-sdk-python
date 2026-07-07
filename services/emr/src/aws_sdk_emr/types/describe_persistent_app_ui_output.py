"""Generated from Smithy shape ``com.amazonaws.emr#DescribePersistentAppUIOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.persistent_app_ui


class DescribePersistentAppUIOutput(TypedDict, closed=True):
    persistent_app_ui: NotRequired[
        "aws_sdk_emr.types.persistent_app_ui.PersistentAppUI"
    ]
    """<p>The persistent application user interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePersistentAppUIOutput) -> dict:
    out: dict = {}
    if "persistent_app_ui" in value:
        import aws_sdk_emr.types.persistent_app_ui

        out["PersistentAppUI"] = (
            aws_sdk_emr.types.persistent_app_ui.serialize_aws_json_1_1(
                value["persistent_app_ui"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePersistentAppUIOutput:
    out: DescribePersistentAppUIOutput = {}  # type: ignore[typeddict-item]
    if "PersistentAppUI" in data:
        import aws_sdk_emr.types.persistent_app_ui

        out["persistent_app_ui"] = (
            aws_sdk_emr.types.persistent_app_ui.deserialize_aws_json_1_1(
                data["PersistentAppUI"]
            )
        )
    return out
