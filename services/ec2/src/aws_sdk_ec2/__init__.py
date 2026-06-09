from __future__ import annotations

from ._auth._identity import Credentials as Credentials
from ._auth._identity import Identity as Identity
from ._auth._providers import (
    CachedProvider as CachedProvider,
)
from ._auth._providers import (
    ChainedProvider as ChainedProvider,
)
from ._auth._providers import (
    CredentialsProvider as CredentialsProvider,
)
from ._auth._providers import (
    EnvCredentialsProvider as EnvCredentialsProvider,
)
from ._auth._providers import (
    IdentityNotFound as IdentityNotFound,
)
from ._auth._providers import (
    IdentityProvider as IdentityProvider,
)
from ._auth._providers import (
    ProfileCredentialsProvider as ProfileCredentialsProvider,
)
from ._auth._providers import (
    StaticAwsCredentialsProvider as StaticAwsCredentialsProvider,
)
from ._auth._signers import Signer as Signer
from ._auth._signers import SigV4Signer as SigV4Signer
from ._services.async_ec2 import AsyncEC2Client as AsyncEC2Client
from ._services.ec2 import EC2Client as EC2Client
