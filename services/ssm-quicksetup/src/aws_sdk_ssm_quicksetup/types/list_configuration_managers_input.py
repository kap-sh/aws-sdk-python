"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListConfigurationManagersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.filters_list


class ListConfigurationManagersInput(TypedDict, closed=True):
    starting_token: NotRequired["str"]
    """<p>The token to use when requesting a specific set of items from a list.</p>"""
    max_items: NotRequired["int"]
    """<p>Specifies the maximum number of configuration managers that are returned by the request.</p>"""
    filters: NotRequired["aws_sdk_ssm_quicksetup.types.filters_list.FiltersList"]
    """<p>Filters the results returned by the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationManagersInput) -> dict:
    out: dict = {}
    if "starting_token" in value:
        out["StartingToken"] = value["starting_token"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "filters" in value:
        import aws_sdk_ssm_quicksetup.types.filters_list

        out["Filters"] = aws_sdk_ssm_quicksetup.types.filters_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListConfigurationManagersInput:
    out: ListConfigurationManagersInput = {}  # type: ignore[typeddict-item]
    if "StartingToken" in data:
        out["starting_token"] = data["StartingToken"]
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "Filters" in data:
        import aws_sdk_ssm_quicksetup.types.filters_list

        out["filters"] = aws_sdk_ssm_quicksetup.types.filters_list.deserialize_json(
            data["Filters"]
        )
    return out
