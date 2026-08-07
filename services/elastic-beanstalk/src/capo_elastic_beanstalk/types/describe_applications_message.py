"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeApplicationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_names_list


class DescribeApplicationsMessage(TypedDict, closed=True):
    application_names: NotRequired[
        "capo_elastic_beanstalk.types.application_names_list.ApplicationNamesList"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeApplicationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_names" in value:
        import capo_elastic_beanstalk.types.application_names_list

        capo_elastic_beanstalk.types.application_names_list.serialize_query(
            value["application_names"], pairs, f"{key_prefix}ApplicationNames"
        )


def deserialize_query(el: Element) -> DescribeApplicationsMessage:
    out: DescribeApplicationsMessage = {}  # type: ignore[typeddict-item]
    child_application_names = el.find("ApplicationNames")
    if child_application_names is not None:
        import capo_elastic_beanstalk.types.application_names_list

        out["application_names"] = (
            capo_elastic_beanstalk.types.application_names_list.deserialize_query(
                child_application_names
            )
        )
    return out
