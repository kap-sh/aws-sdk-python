"""Generated from Smithy shape ``com.amazonaws.s3control#RouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.multi_region_access_point_route

RouteList: TypeAlias = list[
    "capo_s3_control.types.multi_region_access_point_route.MultiRegionAccessPointRoute"
]


# --- restXml ser/de ---
def serialize_xml(value: RouteList, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    for item in value:
        import capo_s3_control.types.multi_region_access_point_route

        capo_s3_control.types.multi_region_access_point_route.serialize_xml(
            item, el, "Route"
        )


def deserialize_xml(el: Element) -> RouteList:
    import capo_s3_control.types.multi_region_access_point_route

    out: RouteList = []
    for child in el.findall("Route"):
        out.append(
            capo_s3_control.types.multi_region_access_point_route.deserialize_xml(child)
        )
    return out


def serialize_xml_flat(value: RouteList, parent: Element, tag: str) -> None:
    """Variant for parents with ``@xmlFlattened`` on the referencing member. Items go directly under ``parent``."""
    for item in value:
        import capo_s3_control.types.multi_region_access_point_route

        capo_s3_control.types.multi_region_access_point_route.serialize_xml(
            item, parent, tag
        )


def deserialize_xml_flat(parent: Element, tag: str) -> RouteList:
    import capo_s3_control.types.multi_region_access_point_route

    out: RouteList = []
    for child in parent.findall(tag):
        out.append(
            capo_s3_control.types.multi_region_access_point_route.deserialize_xml(child)
        )
    return out
