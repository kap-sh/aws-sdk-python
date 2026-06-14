"""Generated from Smithy shape ``com.amazonaws.uxc#GetAccountCustomizationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_uxc.types.account_color
    import aws_sdk_uxc.types.regions_list
    import aws_sdk_uxc.types.service_list


class GetAccountCustomizationsOutput(TypedDict):
    account_color: NotRequired["aws_sdk_uxc.types.account_color.AccountColor"]
    """<p>The account color preference. A value of <code>none</code> indicates that you have not set a color.</p>"""
    visible_services: NotRequired["aws_sdk_uxc.types.service_list.ServiceList"]
    r"""<p>The list of Amazon Web Services service identifiers that are visible to the account in the Amazon Web Services Management Console. A value of <code>null</code> indicates that you have not configured this feature and all services are visible. For valid service identifiers, call <a href=\"https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html\">ListServices</a>.</p>"""
    visible_regions: NotRequired["aws_sdk_uxc.types.regions_list.RegionsList"]
    r"""<p>The list of Amazon Web Services Region codes that are visible to the account in the Amazon Web Services Management Console. A value of <code>null</code> indicates that you have not configured this feature and all Regions are visible. For a list of valid Region codes, see <a href=\"https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html\">Amazon Web Services Regions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountCustomizationsOutput) -> dict:
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


def deserialize_json(data: dict) -> GetAccountCustomizationsOutput:
    out: GetAccountCustomizationsOutput = {}  # type: ignore[typeddict-item]
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
