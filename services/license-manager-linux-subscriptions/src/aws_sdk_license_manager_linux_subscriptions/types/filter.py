"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.operator
    import aws_sdk_license_manager_linux_subscriptions.types.string_list


class Filter(TypedDict):
    name: NotRequired["str"]
    """<p>The type of name to filter by.</p>"""
    values: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.string_list.StringList"
    ]
    """<p>One or more values for the name to filter by.</p>"""
    operator: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.operator.Operator"
    ]
    """<p>An operator for filtering results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.string_list

        out["Values"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_list.serialize_json(
                value["values"]
            )
        )
    if "operator" in value:
        out["Operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Values" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.string_list

        out["values"] = (
            aws_sdk_license_manager_linux_subscriptions.types.string_list.deserialize_json(
                data["Values"]
            )
        )
    if "Operator" in data:
        out["operator"] = data["Operator"]
    return out
