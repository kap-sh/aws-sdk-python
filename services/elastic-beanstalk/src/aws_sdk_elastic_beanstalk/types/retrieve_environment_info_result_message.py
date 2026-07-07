"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#RetrieveEnvironmentInfoResultMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.environment_info_description_list


class RetrieveEnvironmentInfoResultMessage(TypedDict, closed=True):
    environment_info: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_info_description_list.EnvironmentInfoDescriptionList"
    ]
    """<p> The <a>EnvironmentInfoDescription</a> of the environment. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RetrieveEnvironmentInfoResultMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "environment_info" in value:
        import aws_sdk_elastic_beanstalk.types.environment_info_description_list

        aws_sdk_elastic_beanstalk.types.environment_info_description_list.serialize_query(
            value["environment_info"], pairs, f"{prefix}.EnvironmentInfo"
        )


def deserialize_query(el: Element) -> RetrieveEnvironmentInfoResultMessage:
    out: RetrieveEnvironmentInfoResultMessage = {}  # type: ignore[typeddict-item]
    child_environment_info = el.find("EnvironmentInfo")
    if child_environment_info is not None:
        import aws_sdk_elastic_beanstalk.types.environment_info_description_list

        out["environment_info"] = (
            aws_sdk_elastic_beanstalk.types.environment_info_description_list.deserialize_query(
                child_environment_info
            )
        )
    return out
