"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#RetrieveEnvironmentInfoResultMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_info_description_list


class RetrieveEnvironmentInfoResultMessage(TypedDict, closed=True):
    environment_info: NotRequired[
        "capo_elastic_beanstalk.types.environment_info_description_list.EnvironmentInfoDescriptionList"
    ]
    """<p> The <a>EnvironmentInfoDescription</a> of the environment. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RetrieveEnvironmentInfoResultMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "environment_info" in value:
        import capo_elastic_beanstalk.types.environment_info_description_list

        capo_elastic_beanstalk.types.environment_info_description_list.serialize_query(
            value["environment_info"], pairs, f"{key_prefix}EnvironmentInfo"
        )


def deserialize_query(el: Element) -> RetrieveEnvironmentInfoResultMessage:
    out: RetrieveEnvironmentInfoResultMessage = {}  # type: ignore[typeddict-item]
    child_environment_info = el.find("EnvironmentInfo")
    if child_environment_info is not None:
        import capo_elastic_beanstalk.types.environment_info_description_list

        out["environment_info"] = (
            capo_elastic_beanstalk.types.environment_info_description_list.deserialize_query(
                child_environment_info
            )
        )
    return out
