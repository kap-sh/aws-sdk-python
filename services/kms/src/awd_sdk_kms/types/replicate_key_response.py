"""Generated from Smithy shape ``com.amazonaws.kms#ReplicateKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.key_metadata
    import awd_sdk_kms.types.policy_type
    import awd_sdk_kms.types.tag_list


class ReplicateKeyResponse(TypedDict):
    replica_key_metadata: NotRequired["awd_sdk_kms.types.key_metadata.KeyMetadata"]
    """<p>Displays details about the new replica key, including its Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) and <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html\">Key states of KMS keys</a>. It also includes the ARN and Amazon Web Services Region of its primary key and other replica keys.</p>"""
    replica_policy: NotRequired["awd_sdk_kms.types.policy_type.PolicyType"]
    """<p>The key policy of the new replica key. The value is a key policy document in JSON format.</p>"""
    replica_tags: NotRequired["awd_sdk_kms.types.tag_list.TagList"]
    """<p>The tags on the new replica key. The value is a list of tag key and tag value pairs.</p>"""
