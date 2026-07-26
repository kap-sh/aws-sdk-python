"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AvailableSolutionStackNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.solution_stack_name

AvailableSolutionStackNamesList: TypeAlias = list[
    "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableSolutionStackNamesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> AvailableSolutionStackNamesList:
    out: AvailableSolutionStackNamesList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AvailableSolutionStackNamesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(
    parent: Element, tag: str
) -> AvailableSolutionStackNamesList:
    out: AvailableSolutionStackNamesList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
