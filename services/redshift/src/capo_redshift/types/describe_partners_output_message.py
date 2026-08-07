"""Generated from Smithy shape ``com.amazonaws.redshift#DescribePartnersOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.partner_integration_info_list


class DescribePartnersOutputMessage(TypedDict, closed=True):
    partner_integration_info_list: NotRequired[
        "capo_redshift.types.partner_integration_info_list.PartnerIntegrationInfoList"
    ]
    """<p>A list of partner integrations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePartnersOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "partner_integration_info_list" in value:
        import capo_redshift.types.partner_integration_info_list

        capo_redshift.types.partner_integration_info_list.serialize_query(
            value["partner_integration_info_list"],
            pairs,
            f"{key_prefix}PartnerIntegrationInfoList",
        )


def deserialize_query(el: Element) -> DescribePartnersOutputMessage:
    out: DescribePartnersOutputMessage = {}  # type: ignore[typeddict-item]
    child_partner_integration_info_list = el.find("PartnerIntegrationInfoList")
    if child_partner_integration_info_list is not None:
        import capo_redshift.types.partner_integration_info_list

        out["partner_integration_info_list"] = (
            capo_redshift.types.partner_integration_info_list.deserialize_query(
                child_partner_integration_info_list
            )
        )
    return out
