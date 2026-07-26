"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CustomAmiList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.custom_ami

CustomAmiList: TypeAlias = list["capo_elastic_beanstalk.types.custom_ami.CustomAmi"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomAmiList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.custom_ami

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.custom_ami.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CustomAmiList:
    import capo_elastic_beanstalk.types.custom_ami

    out: CustomAmiList = []
    for child in el.findall("member"):
        out.append(capo_elastic_beanstalk.types.custom_ami.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CustomAmiList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.custom_ami

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.custom_ami.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CustomAmiList:
    import capo_elastic_beanstalk.types.custom_ami

    out: CustomAmiList = []
    for child in parent.findall(tag):
        out.append(capo_elastic_beanstalk.types.custom_ami.deserialize_query(child))
    return out
