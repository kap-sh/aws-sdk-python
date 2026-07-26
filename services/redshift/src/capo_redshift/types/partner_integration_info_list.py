"""Generated from Smithy shape ``com.amazonaws.redshift#PartnerIntegrationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.partner_integration_info

PartnerIntegrationInfoList: TypeAlias = list[
    "capo_redshift.types.partner_integration_info.PartnerIntegrationInfo"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PartnerIntegrationInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.partner_integration_info

    for n, item in enumerate(value, 1):
        capo_redshift.types.partner_integration_info.serialize_query(
            item, pairs, f"{prefix}.PartnerIntegrationInfo.{n}"
        )


def deserialize_query(el: Element) -> PartnerIntegrationInfoList:
    import capo_redshift.types.partner_integration_info

    out: PartnerIntegrationInfoList = []
    for child in el.findall("PartnerIntegrationInfo"):
        out.append(
            capo_redshift.types.partner_integration_info.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: PartnerIntegrationInfoList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.partner_integration_info

    for n, item in enumerate(value, 1):
        capo_redshift.types.partner_integration_info.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PartnerIntegrationInfoList:
    import capo_redshift.types.partner_integration_info

    out: PartnerIntegrationInfoList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.partner_integration_info.deserialize_query(child)
        )
    return out
