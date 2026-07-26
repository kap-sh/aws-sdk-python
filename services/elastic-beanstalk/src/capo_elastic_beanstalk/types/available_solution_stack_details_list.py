"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#AvailableSolutionStackDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.solution_stack_description

AvailableSolutionStackDetailsList: TypeAlias = list[
    "capo_elastic_beanstalk.types.solution_stack_description.SolutionStackDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableSolutionStackDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.solution_stack_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.solution_stack_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AvailableSolutionStackDetailsList:
    import capo_elastic_beanstalk.types.solution_stack_description

    out: AvailableSolutionStackDetailsList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.solution_stack_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: AvailableSolutionStackDetailsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.solution_stack_description

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.solution_stack_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> AvailableSolutionStackDetailsList:
    import capo_elastic_beanstalk.types.solution_stack_description

    out: AvailableSolutionStackDetailsList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.solution_stack_description.deserialize_query(
                child
            )
        )
    return out
