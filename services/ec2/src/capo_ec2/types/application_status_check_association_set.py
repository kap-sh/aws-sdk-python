"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusCheckAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_association_object

ApplicationStatusCheckAssociationSet: TypeAlias = list[
    "capo_ec2.types.application_status_check_association_object.ApplicationStatusCheckAssociationObject"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplicationStatusCheckAssociationSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.application_status_check_association_object

        capo_ec2.types.application_status_check_association_object.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ApplicationStatusCheckAssociationSet:
    import capo_ec2.types.application_status_check_association_object

    out: ApplicationStatusCheckAssociationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.application_status_check_association_object.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ApplicationStatusCheckAssociationSet:
    import capo_ec2.types.application_status_check_association_object

    out: ApplicationStatusCheckAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.application_status_check_association_object.deserialize_ec2_query(
                child
            )
        )
    return out
