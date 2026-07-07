"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListQuickSetupTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.quick_setup_type_list


class ListQuickSetupTypesOutput(TypedDict, closed=True):
    quick_setup_type_list: NotRequired[
        "aws_sdk_ssm_quicksetup.types.quick_setup_type_list.QuickSetupTypeList"
    ]
    """<p>An array of Quick Setup types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuickSetupTypesOutput) -> dict:
    out: dict = {}
    if "quick_setup_type_list" in value:
        import aws_sdk_ssm_quicksetup.types.quick_setup_type_list

        out["QuickSetupTypeList"] = (
            aws_sdk_ssm_quicksetup.types.quick_setup_type_list.serialize_json(
                value["quick_setup_type_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListQuickSetupTypesOutput:
    out: ListQuickSetupTypesOutput = {}  # type: ignore[typeddict-item]
    if "QuickSetupTypeList" in data:
        import aws_sdk_ssm_quicksetup.types.quick_setup_type_list

        out["quick_setup_type_list"] = (
            aws_sdk_ssm_quicksetup.types.quick_setup_type_list.deserialize_json(
                data["QuickSetupTypeList"]
            )
        )
    return out
