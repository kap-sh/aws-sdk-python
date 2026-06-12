"""Generated from Smithy shape ``com.amazonaws.redshift#DescribePartnersOutputMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.partner_integration_info_list


class DescribePartnersOutputMessage(TypedDict):
    partner_integration_info_list: NotRequired[
        "aws_sdk_redshift.types.partner_integration_info_list.PartnerIntegrationInfoList"
    ]
    """<p>A list of partner integrations.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePartnersOutputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "partner_integration_info_list" in value:
        import aws_sdk_redshift.types.partner_integration_info_list

        aws_sdk_redshift.types.partner_integration_info_list.serialize_query(
            value["partner_integration_info_list"],
            pairs,
            f"{prefix}.PartnerIntegrationInfoList",
        )


def deserialize_query(el: Element) -> DescribePartnersOutputMessage:
    out: DescribePartnersOutputMessage = {}  # type: ignore[typeddict-item]
    child_partner_integration_info_list = el.find("PartnerIntegrationInfoList")
    if child_partner_integration_info_list is not None:
        import aws_sdk_redshift.types.partner_integration_info_list

        out["partner_integration_info_list"] = (
            aws_sdk_redshift.types.partner_integration_info_list.deserialize_query(
                child_partner_integration_info_list
            )
        )
    return out
