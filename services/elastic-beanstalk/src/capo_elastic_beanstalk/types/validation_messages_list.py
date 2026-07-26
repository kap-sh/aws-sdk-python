"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ValidationMessagesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.validation_message

ValidationMessagesList: TypeAlias = list[
    "capo_elastic_beanstalk.types.validation_message.ValidationMessage"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidationMessagesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.validation_message

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.validation_message.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ValidationMessagesList:
    import capo_elastic_beanstalk.types.validation_message

    out: ValidationMessagesList = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_beanstalk.types.validation_message.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ValidationMessagesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elastic_beanstalk.types.validation_message

    for n, item in enumerate(value, 1):
        capo_elastic_beanstalk.types.validation_message.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ValidationMessagesList:
    import capo_elastic_beanstalk.types.validation_message

    out: ValidationMessagesList = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_beanstalk.types.validation_message.deserialize_query(child)
        )
    return out
