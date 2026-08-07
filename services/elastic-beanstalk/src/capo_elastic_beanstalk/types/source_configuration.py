"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_template_name


class SourceConfiguration(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application associated with the configuration.</p>"""
    template_name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>The name of the configuration template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_name" in value:
        pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))


def deserialize_query(el: Element) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    return out
