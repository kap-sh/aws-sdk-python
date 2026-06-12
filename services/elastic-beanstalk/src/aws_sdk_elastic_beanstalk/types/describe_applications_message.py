"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeApplicationsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_names_list


class DescribeApplicationsMessage(TypedDict):
    application_names: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_names_list.ApplicationNamesList"
    ]
    """<p>If specified, AWS Elastic Beanstalk restricts the returned descriptions to only include those with the specified names.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeApplicationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_names" in value:
        import aws_sdk_elastic_beanstalk.types.application_names_list

        aws_sdk_elastic_beanstalk.types.application_names_list.serialize_query(
            value["application_names"], pairs, f"{prefix}.ApplicationNames"
        )


def deserialize_query(el: Element) -> DescribeApplicationsMessage:
    out: DescribeApplicationsMessage = {}  # type: ignore[typeddict-item]
    child_application_names = el.find("ApplicationNames")
    if child_application_names is not None:
        import aws_sdk_elastic_beanstalk.types.application_names_list

        out["application_names"] = (
            aws_sdk_elastic_beanstalk.types.application_names_list.deserialize_query(
                child_application_names
            )
        )
    return out
