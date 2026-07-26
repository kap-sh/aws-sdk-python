"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointRegionalResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.multi_region_access_point_regional_response

MultiRegionAccessPointRegionalResponseList: TypeAlias = list[
    "capo_s3_control.types.multi_region_access_point_regional_response.MultiRegionAccessPointRegionalResponse"
]


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointRegionalResponseList, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.multi_region_access_point_regional_response

        capo_s3_control.types.multi_region_access_point_regional_response.serialize_xml(
            item, el, "Region"
        )


def deserialize_xml(el: Element) -> MultiRegionAccessPointRegionalResponseList:
    import capo_s3_control.types.multi_region_access_point_regional_response

    out: MultiRegionAccessPointRegionalResponseList = []
    for child in el.findall("Region"):
        out.append(
            capo_s3_control.types.multi_region_access_point_regional_response.deserialize_xml(
                child
            )
        )
    return out


def serialize_xml_flat(
    value: MultiRegionAccessPointRegionalResponseList, parent: Element, tag: str
) -> None:
    """Variant used by parent structures with ``@xmlFlattened`` on the referencing member. Items emitted directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.multi_region_access_point_regional_response

        capo_s3_control.types.multi_region_access_point_regional_response.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(
    parent: Element, tag: str
) -> MultiRegionAccessPointRegionalResponseList:
    import capo_s3_control.types.multi_region_access_point_regional_response

    out: MultiRegionAccessPointRegionalResponseList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.multi_region_access_point_regional_response.deserialize_xml(
                child
            )
        )
    return out
