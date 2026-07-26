"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeEnvironmentHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.environment_health_attributes
    import capo_elastic_beanstalk.types.environment_id
    import capo_elastic_beanstalk.types.environment_name


class DescribeEnvironmentHealthRequest(TypedDict, closed=True):
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>Specify the environment by name.</p> <p>You must specify either this or an EnvironmentName, or both.</p>"""
    environment_id: NotRequired[
        "capo_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>Specify the environment by ID.</p> <p>You must specify either this or an EnvironmentName, or both.</p>"""
    attribute_names: NotRequired[
        "capo_elastic_beanstalk.types.environment_health_attributes.EnvironmentHealthAttributes"
    ]
    """<p>Specify the response elements to return. To retrieve all attributes, set to <code>All</code>. If no attribute names are specified, returns the name of the environment.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEnvironmentHealthRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "attribute_names" in value:
        import capo_elastic_beanstalk.types.environment_health_attributes

        capo_elastic_beanstalk.types.environment_health_attributes.serialize_query(
            value["attribute_names"], pairs, f"{prefix}.AttributeNames"
        )


def deserialize_query(el: Element) -> DescribeEnvironmentHealthRequest:
    out: DescribeEnvironmentHealthRequest = {}  # type: ignore[typeddict-item]
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_attribute_names = el.find("AttributeNames")
    if child_attribute_names is not None:
        import capo_elastic_beanstalk.types.environment_health_attributes

        out["attribute_names"] = (
            capo_elastic_beanstalk.types.environment_health_attributes.deserialize_query(
                child_attribute_names
            )
        )
    return out
