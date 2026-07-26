"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketLifecycleConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.transition_default_minimum_object_size


class PutBucketLifecycleConfigurationOutput(TypedDict, closed=True):
    transition_default_minimum_object_size: NotRequired[
        "capo_s3.types.transition_default_minimum_object_size.TransitionDefaultMinimumObjectSize"
    ]
    """<p>Indicates which default minimum object size behavior is applied to the lifecycle configuration.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note> <ul> <li> <p> <code>all_storage_classes_128K</code> - Objects smaller than 128 KB will not transition to any storage class by default. </p> </li> <li> <p> <code>varies_by_storage_class</code> - Objects smaller than 128 KB will transition to Glacier Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes will prevent transitions smaller than 128 KB. </p> </li> </ul> <p>To customize the minimum object size for any transition you can add a filter that specifies a custom <code>ObjectSizeGreaterThan</code> or <code>ObjectSizeLessThan</code> in the body of your transition rule. Custom filters always take precedence over the default transition behavior.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutBucketLifecycleConfigurationOutput, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> PutBucketLifecycleConfigurationOutput:
    out: PutBucketLifecycleConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
