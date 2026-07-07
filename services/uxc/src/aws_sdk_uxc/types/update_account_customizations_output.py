"""Generated from Smithy shape ``com.amazonaws.uxc#UpdateAccountCustomizationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_uxc.types.account_color
    import aws_sdk_uxc.types.regions_list
    import aws_sdk_uxc.types.service_list


class UpdateAccountCustomizationsOutput(TypedDict, closed=True):
    account_color: NotRequired["aws_sdk_uxc.types.account_color.AccountColor"]
    """<p>The current account color preference after the update.</p>"""
    visible_services: NotRequired["aws_sdk_uxc.types.service_list.ServiceList"]
    """<p>The current list of visible service identifiers after the update.</p>"""
    visible_regions: NotRequired["aws_sdk_uxc.types.regions_list.RegionsList"]
    """<p>The current list of visible Region codes after the update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomizationsOutput) -> dict:
    out: dict = {}
    if "account_color" in value:
        import aws_sdk_uxc.types.account_color

        out["accountColor"] = aws_sdk_uxc.types.account_color.serialize_json(
            value["account_color"]
        )
    if "visible_services" in value:
        import aws_sdk_uxc.types.service_list

        out["visibleServices"] = aws_sdk_uxc.types.service_list.serialize_json(
            value["visible_services"]
        )
    if "visible_regions" in value:
        import aws_sdk_uxc.types.regions_list

        out["visibleRegions"] = aws_sdk_uxc.types.regions_list.serialize_json(
            value["visible_regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomizationsOutput:
    out: UpdateAccountCustomizationsOutput = {}  # type: ignore[typeddict-item]
    if "accountColor" in data:
        import aws_sdk_uxc.types.account_color

        out["account_color"] = aws_sdk_uxc.types.account_color.deserialize_json(
            data["accountColor"]
        )
    if "visibleServices" in data:
        import aws_sdk_uxc.types.service_list

        out["visible_services"] = aws_sdk_uxc.types.service_list.deserialize_json(
            data["visibleServices"]
        )
    if "visibleRegions" in data:
        import aws_sdk_uxc.types.regions_list

        out["visible_regions"] = aws_sdk_uxc.types.regions_list.deserialize_json(
            data["visibleRegions"]
        )
    return out
